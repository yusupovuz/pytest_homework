from sum_array import sum_array

def test_a1():
    a = []
    assert sum_array(a) == 0

def test_a2():
    a = [-1,2,-4]
    assert sum_array(a) == -3

def test_a3():
    assert sum_array(range(101)) == 5050