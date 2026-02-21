from banjo import are_you_playing_banjo

def test_a1():
    name = 'roma'
    assert are_you_playing_banjo(name) == 'roma plays banjo'

def test_a2():
    name = 'bob'
    assert are_you_playing_banjo(name) == 'bob does not play banjo'

def test_a3():
    name = 'Rokky'
    assert are_you_playing_banjo(name) == 'Rokky plays banjo'