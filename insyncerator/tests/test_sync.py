import pytest
import asyncio

from .. import Sync

class SomeClass:

    def __init__(self, x):
        self.x = x

    def get_x(self):
        return self.x

    async def sleep_then_x(self, sleep_time):
        await asyncio.sleep(sleep_time)
        return self.get_x()

    async def sleep_then_x_twice(self, sleep_time):
        a = await(self.sleep_then_x(sleep_time))
        b = await(self.sleep_then_x(sleep_time))
        return a + b

    sync = Sync()


def test_sync():
    obj = SomeClass(x=5)
    assert obj.get_x() == 5

    assert obj.sync.sleep_then_x(0.01) == 5
    assert obj.sync.sleep_then_x_twice(0.01) == 10


def test_sync_doesnt_work_on_already_sync_method():

    obj = SomeClass(5)
    with pytest.raises(TypeError):
        obj.sync.get_x()
