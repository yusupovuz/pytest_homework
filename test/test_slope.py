from slope import find_slope

def test_a1():
    assert find_slope([19,3,20,3]) == '0'

def test_a2():
    assert find_slope([-7,2,-7,4]) == 'undefined'
