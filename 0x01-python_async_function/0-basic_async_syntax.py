#!/usr/bin/env python3
"""
This module contains an asynchronous coroutine that waits for a random delay
and returns the delay value.
"""

import asyncio
import random
from typing import Union

async def wait_random(max_delay: int = 10) -> Union[float, int]:
    """
    Asynchronous coroutine that waits for a random delay between 0 and max_delay
    (inclusive) and returns the delay value.
    
    Args:
        max_delay (int): Maximum delay value (default is 10).
    
    Returns:
        float: The actual delay value.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

