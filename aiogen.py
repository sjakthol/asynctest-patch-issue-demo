import asyncio

@asyncio.coroutine
def generate():
    yield from asyncio.sleep(0.1)
    return "original"

def generate_sync():
    return "original"
