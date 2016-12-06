from asyncio import get_event_loop
from collections import Awaitable


class Sync:

    def __init__(self, loop=None):
        self._loop = loop

    def __get__(self, instance, owner):
        return _SyncDescriptor(instance, self._loop)

    def __set__(self, instance, owner, value):
        raise AttributeError("Can't set into Sync objects.")

    def __del__(self, instance, owner):
        raise AttributeError("Can't set into Sync objects.")


class _SyncDescriptor:

    def __init__(self, instance, loop):
        self._instance = instance
        self._loop = loop

    def __call__(self, loop):
        return SyncCoroutine(self._instance, loop)

    def __getattr__(self, name):
        func = getattr(self._instance, name)
        return SyncCoroutine(func, loop=self._loop, name=name)


class SyncCoroutine:
    """A Synchronous proxy around a coroutine.
    """
    def __init__(self, func, loop, name):
        self._func = func
        self._loop = loop
        self._name = name

    def __call__(self, *args, **kwargs):
        loop = get_event_loop() if self._loop is None else self._loop
        awaitable = self._func(*args, **kwargs)

        if not isinstance(awaitable, Awaitable):
            raise TypeError("%r did not return an awaitable" % self._name)

        return loop.run_until_complete(awaitable)
