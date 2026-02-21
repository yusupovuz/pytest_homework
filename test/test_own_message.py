from own_message import greet

def test_a1():
    assert greet('Roy','Bob') == 'Hello guest'

def test_a2():
    assert greet('Jack','Jack') == 'Hello boss'
def test_a3():
    assert greet('John','Joe') == 'Hello guest'