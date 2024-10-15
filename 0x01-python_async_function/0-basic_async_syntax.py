#!/usr/bin/python3
import asyncio
import random
"""
This module contains an asynchronous function 'wait_random'
which waits for a random delay between 0 and 'max_delay' seconds
and returns the delay value.

Functions:
    - wait_random(max_delay: int = 10) -> float
"""

async def wait_random(max_delay: int = 10) -> float:
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
