import asyncio
import logging
from cbutil import *

proj_root_path = Path(__file__).prnt.prnt
test_tmp_path = proj_root_path/Path('tmp/test')

async def atest_init():
    logging.info('init success')
    

def test_init():
    asyncio.run(atest_init())