import asyncio
import requests


async def get_request(url):
    data = requests.get_request(url)
    return url

async def waiter(event):
    print('> waiting for it ...')
    await event.wait()
    print('> ... got it!')

# async def main():
#     # Create an Event object.
#     event = asyncio.Event()
#
#     # Spawn a Task to wait until 'event' is set.
#     waiter_task = asyncio.create_task(waiter(event))
#     print('going to sleep')
#     # Sleep for 1 second and set the event.
#     await asyncio.sleep(1)
#     event.set()
#     print('event set')
#     # Wait until the waiter task is finished.
#     await waiter_task

import asyncio
import aiohttp  # pip install aiohttp aiodns


async def get(session: aiohttp.ClientSession, query: str):
    url = f"http://humanyze.com"
    print(f"Requesting {url}")
    resp = await session.request('GET', url=url)
    # Note that this may raise an exception for non-2xx responses
    print(resp, resp.__class__)
    # data = await resp.json(content_type='text/html')
    print(f"Received data for {url}")
    return resp


async def main(colors):
    # Asynchronous context manager.  Prefer this rather
    # than using a different session for each GET request
    async with aiohttp.ClientSession() as session:
        tasks = []
        for c in colors:
            tasks.append(get(session=session, query=c))
        # asyncio.gather() will wait on the entire task set to be completed
        htmls = [await _ for _ in asyncio.as_completed(tasks)]
        print(f'htmls -> {htmls}')
        return htmls


if __name__ == '__main__':
    colors = ['red', 'blue', 'green']  # ...
    # Either take colors from stdin or make some default here
    asyncio.run(main(colors))  # Python 3.7+
