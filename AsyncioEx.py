#!/usr/bin/env python

"""AsyncioEx.py: Demo code for Async IO"""
__author__ = "Sumit Kala"

import asyncio
import time

def sync_f():
    print("one",end='')
    time.sleep(1)
    print("Two",end="")

async def async_f():
    print("One",end="")
    await asyncio.sleep(1)
    print("Two",end="")

async def main():
    #async_f()
    await asyncio.gather(async_f(),async_f(),async_f())


if __name__ == '__main__':
    asyncio.run(main())