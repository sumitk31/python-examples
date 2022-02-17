#!/usr/bin/env python3
# rand.py

import asyncio
import random
import aiohttp
import time
import requests

def syncgethtml(url):
    r = requests.get(url)
    print("Status:", r.status_code)
    print("Content-type:", r.headers['content-type'])
    r.close()

async def gethtml(url):
    session = aiohttp.ClientSession()
    response = await session.get(url)
    print(url)
    print("Async Status:", response.status)
    print("Async Content-type:", response.headers['content-type'])
    response.close()
    await session.close()

    return
    '''
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:

         print("Async Status:", response.status)
         print("Async Content-type:", response.headers['content-type'])
    '''

async def main():
    t1 = time.time()
    await asyncio.gather(gethtml("http://google.com"),
                         gethtml("http://python.org"),
                         gethtml("http://facebook.com"),
                         gethtml("http://google.com"),
                         gethtml("http://python.org"),
                         gethtml("http://facebook.com"))

    t2 = time.time()
    print(f'Elapsed time {t2-t1}')

    t1 = time.time()
    syncgethtml("http://google.com")
    syncgethtml("http://python.org")
    syncgethtml("http://facebook.com")
    syncgethtml("http://google.com")
    syncgethtml("http://python.org")
    syncgethtml("http://facebook.com")
    t2 = time.time()
    #time.sleep(5)
    print(f'Elapsed time {t2 - t1}')

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    #asyncio.run(main())


