``insyncerator``
================

``insyncerator`` is a library that makes it convenient to call asynchronous
object methods from synchronous contexts.  This is particularly useful for
interactively debugging asynchronous code in the Python REPL.

Usage
~~~~~

``insyncerator`` has just one entrypoint, the ``Sync`` class.  To use it,
assign an instance of ``Sync`` as class attribute of a type with ``async def``
methods::

  import asyncio
  from insyncerator import Sync

  class AsyncClass:

      def __init__(self, x):
          self.x = x

      async def get_x(self):
          await asyncio.sleep(1)
          return x

      sync = Sync()

Normally, if we wanted to test ``get_x`` in the Python REPL, we would have to
do so like this::

  >>> obj = AsyncClass(5)
  >>> from asyncio import get_event_loop
  >>> loop = get_event_loop()
  >>> loop.run_until_complete(obj.get_x())
  5

With the addition of our ``sync`` descriptor, however, the above code can be
shortened to just::

  >>> obj = AsyncClass(5)
  >>> obj.sync.get_x()
  5
