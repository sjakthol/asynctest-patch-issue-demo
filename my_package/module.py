import asyncio
import sync_package.gen
import async_package.gen


@asyncio.coroutine
def method_async():
    return (yield from async_package.gen.generate())


def method_sync():
    return sync_package.gen.generate()
