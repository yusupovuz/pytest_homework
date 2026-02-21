from combat import combat

def test_a1():
    assert combat(100,80) == 20

def test_a2():
    assert combat(50,49) == 1

def test_a3():
    assert combat(20,30) == 0
