import asyncio
import random
import time
import logging

from cbutil import CoroExecutor

print = logging.info

async def assignment(i, t):
    print(f'id: {i}, time: {t}, begin')
    await asyncio.sleep(t)
    print(f'id: {i}, time: {t}, end')
    return i, t


async def atest_submit():
    executor = CoroExecutor()
    ts = [random.random()*3 for i in range(20)]
    time_start = time.time()
    futures = [await executor.submit(assignment(i, ts[i])) for i in range(20)]
    results = [await future for future in futures]
    time_end = time.time()
    print(results)
    print(f'time: {time_end-time_start}')
    # await executor.wait_done()

async def atest_submit_nw():
    executor = CoroExecutor()
    ts = [random.random()*3 for i in range(20)]
    time_start = time.time()
    results = [await executor.submit_nw(assignment(i, ts[i])) for i in range(20)]
    time_end = time.time()
    print(results)
    print(f'time: {time_end-time_start}')

async def atest_submit_nw_one():
    n = 1
    executor = CoroExecutor()
    ts = [random.random()*3 for i in range(n)]
    time_start = time.time()
    results = [await executor.submit_nw(assignment(i, ts[i])) for i in range(n)]
    time_end = time.time()
    print(results)
    print(f'time: {time_end-time_start}')



def test():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(atest_submit())


    