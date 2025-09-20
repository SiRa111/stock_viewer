from datetime import date
from seasons import minutes_since_birth, number_to_words

def test_minutes_since_birth():
    today = date(2000, 1, 1)
    birth = date(1999, 1, 1)
    assert minutes_since_birth(birth, today) == 525600

    birth = date(1995, 1, 1)
    assert minutes_since_birth(birth, today) == 2629440

def test_number_to_words():
    assert number_to_words(525600).startswith("Five hundred")
    assert number_to_words(1051200).startswith("One million")
    assert number_to_words(2629440).startswith("Two million")
