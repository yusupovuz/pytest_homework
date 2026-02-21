from rpg import playerRankUp

def test_a1():
    assert playerRankUp(64) == False
def test_a2():
    assert playerRankUp(120) == 'Well done! You have advanced to the qualifying stage. Win 2 out of your next 3 games to rank up.'
