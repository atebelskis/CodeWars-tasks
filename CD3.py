import pytest

def generator(From, To, Step):
    b = []
    a = From - Step
    while From <= To:
        a += Step
        b.append(a)
        if a == To:
            break
    return b

def test_g():
    assert generator(10,20,1) == [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


def last_survivor(letters, coords):
    a = list(letters.split())
    #b = enumerate(a)
    for i in coords and i in enumerate(a):
        #if i in coords:
        a.remove(i)
            #coords.remove(i)
    return a
@pytest.mark.skip
def test_ls():
    assert last_survivor('abc', [1, 1]) == 'a'

from math import modf


def convert(deg):
    a = list(modf(deg))
    return a

def convert2(deg):
    a = int(deg)
    b = deg - a
    c = b*0.6
    d = deg - a - c

    return a,round(c, 2),d




def test_con():
    assert convert(20.34) == (0.34, 20.0)

def test_con2():
    assert convert2(40.567) == (40, 34, 1)

def test_con3():
    assert convert2(20.999) == (20, 59, 56)