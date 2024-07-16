from plates import is_valid


def test_alpha():
    assert is_valid("q") == False
    assert is_valid("QWERTYU") == False
    assert is_valid("QWerTy") == False


def test_first_two():
    assert is_valid("54gh") == False
    assert is_valid("jk") == True
    assert is_valid("jkl90") == True
    assert is_valid("34567") == False


def test_only_alnum():
    assert is_valid("gh_ij") == False
    assert is_valid("whoa:90") == False
    assert is_valid("welp./87") == False
    assert is_valid("ghj980") == True


def test_first_non_zero():
    assert is_valid("gh009") == False
    assert is_valid("gh909") == True


def test_end_num():
    assert is_valid("gh09ji") == False
    assert is_valid("ghji90") == True
