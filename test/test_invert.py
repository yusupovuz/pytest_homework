from invert import invert

def test_a1():
    assert invert([1,2,3,4,5]) == [-1,-2,-3,-4,-5]
def test_a2():
    assert invert([]) == []