from practice import add, div

def test_add():
    assert add(4, 5) == 9
    assert add(3, 7) == 10

def test_div():
    assert div(6, 2) == 3
    assert div(4, 0) == 2