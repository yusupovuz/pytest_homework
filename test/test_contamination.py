from contamination import contamination

def test_a1():
    assert contamination("abc","z") =='zzz'
def test_a2():
    assert contamination("","z") ==''

def test_a3():
    assert contamination("//case"," ") =='      '