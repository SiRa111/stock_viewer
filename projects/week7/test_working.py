from working import convert

def test_format():
    assert convert("9:60 AM to 5:60 PM") == ValueError
    assert convert("9 AM - 5 PM ") == ValueError
    assert convert("9:00 AM - 5:00 PM") == ValueError

