from margin import close_compare

def test_a1():
    assert close_compare(2, 5, 3) == 0
def test_a2():
    assert close_compare(4,5) == -1
    