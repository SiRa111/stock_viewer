from datetime import date
from seasons import get_minutes_since_birth, minutes_to_words

def test_get_minutes_since_birth():
    test_date = date.today()
    minutes = get_minutes_since_birth(test_date)
    assert minutes == 0

    test_date = date.fromordinal(date.today().toordinal() - 1)
    minutes = get_minutes_since_birth(test_date)
    assert minutes == 1440

    test_date = date.fromordinal(date.today().toordinal() - 2)
    minutes = get_minutes_since_birth(test_date)
    assert minutes == 2880

def test_minutes_to_words():
    assert minutes_to_words(1440) == "One thousand, four hundred forty"
    assert minutes_to_words(1) == "One"
    assert minutes_to_words(525600) == "Five hundred twenty-five thousand, six hundred"
    assert minutes_to_words(0) == "Zero"

def test_combined_functions():
    test_date = date.today()
    minutes = get_minutes_since_birth(test_date)
    words = minutes_to_words(minutes)
    assert isinstance(words, str)
    assert "minutes" not in words
