import asyncio
import logging
from cbutil import *

proj_root_path = Path(__file__).prnt.prnt
test_tmp_path = proj_root_path/Path('tmp/test')



def test_path():
    f = test_tmp_path/'123'
    f.write_text('2313231312')
    f.touch()
    f.make_copy('342334')


