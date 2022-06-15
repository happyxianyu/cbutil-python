from cbutil.util.adaptor import *


def test_DictObjectAdaptor():
    class A:
        pass
    x = A()
    x.a = 1
    x.b = 2
    y = A()
    y.a = 3
    y.b = 3

    x_ = DictObjectAdaptor(x, ['a', 'b'])
    y_ = DictObjectAdaptor(y, ['b'])
    x_.update(y_)
    assert x.b == 3
    assert x.a == 1


