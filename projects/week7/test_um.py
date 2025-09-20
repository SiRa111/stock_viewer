from um import count


def test_single_um():
    assert count("um") == 1
    assert count("Um?") == 1
    assert count("hello, um, world") == 1


def test_multiple_um():
    assert count("um, thanks, um...") == 2
    assert count("Um, thanks for the album. Um, yeah.") == 2


def test_no_um():
    assert count("yummy") == 0
    assert count("umbrella") == 0
    assert count("humble") == 0


def test_case_insensitive():
    assert count("UM") == 1
    assert count("uM uM Um") == 3
