from get_floor import get_real_floor

def test_a1():
    assert get_real_floor(-1) == -1
def test_a2():
    assert get_real_floor(5) == 4
def test_a3():
    assert get_real_floor(15) == 13