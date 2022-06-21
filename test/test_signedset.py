from cbutil.container import SignedSet
from pprint import pprint


def test_signedset():
    a = SignedSet('abcdefg')
    b = SignedSet('efghijk')


    results = [
        [a|b,a&b,a-b,a^b],
        [-a|b,-a&b,a-b,-a^b],
        [-a|-b,-a&-b,a-b,-a^-b],
        [a|-b,a& -b,a- -b,a^-b]
    ] 
    pprint(results)