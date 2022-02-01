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
    asyncio.sleep(1)
    print("Two",end="")

def main()
    sync_f()