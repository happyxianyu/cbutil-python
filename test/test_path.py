import asyncio
import logging
from cbutil import *

proj_root_path = Path(__file__).prnt.prnt
test_tmp_path = proj_root_path/Path('tmp/test/path')

def test_make_copy():
    test_tmp_path.mkdir()
    f1 = test_tmp_path/'123'
    f2 = f1.prnt/'223'
    t1=  '3213213'
    f1.write_text(t1, encoding='utf8')
    f1.make_copy(f2.name)
    t2 = f2.read_text(encoding='utf8')
    assert t1 == t2


def test_move_to():
    test_tmp_path.remove()
    p1 = test_tmp_path/'1/x'
    ps1 = [p1/str(v) for v in range(10)]
    for p in ps1:
        p.mkdir()
    p2 = test_tmp_path/'2/x'
    p1.move_to(p2.prnt)
    assert p2.exists()


def test_copy_to():
    test_path = test_tmp_path/'test_copy_to'
    test_path.remove()
    p1 = test_path/'1/x'
    ps1 = [p1/str(v) for v in range(10)]
    for p in ps1:
        p.mkdir()
    p2 = test_path/'2/x'
    p1.copy_to(p2.prnt)
    assert p2.exists()

def test_copy_sons_to():
    test_path = test_tmp_path/'test_copy_sons_to'
    test_path.remove()
    p1 = test_path/'1/x'
    ps1 = [p1/str(v) for v in range(10)]
    for p in ps1:
        p.mkdir()
    p2 = test_path/'2/x'
    p1.copy_sons_to(p2)
    assert (p2/'1').exists()

def test_open():
    test_path = test_tmp_path/'3'
    p_n = test_path/'n.txt'
    p_rn = test_path/'rn.txt'
    p_n.write('\n')
    assert '\n' == p_n.read_text()
    p_rn.write('\r\n')
    assert '\r\n' == p_rn.read_text()
    b = test_path/'b.txt'
    b.write('你好'.encode())
    assert '你好'.encode() == b.read_bytes()

