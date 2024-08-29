from working import convert

def test_format():
    assert convert("9:60 AM to 5:60 PM") == False
    assert convert("9 AM - 5 PM ") == False
    assert convert("9:00 AM - 5:00 PM") == False

