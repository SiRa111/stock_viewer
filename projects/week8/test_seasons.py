from datetime import date, timedelta
from seasons import minutes_since_birth, number_to_words

def test_minutes_since_birth():
    today = date.today()
    birth = today - timedelta(days=1)
    assert minutes_since_birth(birth) == 24*60

    birth = today - timedelta(days=365)
    assert minutes_since_birth(birth) == 365*24*60

def test_number_to_words():
    assert number_to_words(525600) == "five hundred twenty five thousand six hundred"
    assert number_to_words(1440) == "one thousand four hundred forty"
