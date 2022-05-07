from cbutil.container import SignSet
from pprint import pprint


def test_signset():
    a = SignSet('abcdefg')
    b = SignSet('efghijk')


    results = [
        [a|b,a&b,a-b,a^b],
        [-a|b,-a&b,a-b,-a^b],
        [-a|-b,-a&-b,a-b,-a^-b],
        [a|-b,a& -b,a- -b,a^-b]
    ] 
    pprint(results)