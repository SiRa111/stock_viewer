from working import convert

def test_format():
    # Invalid cases (should raise ValueError)
    try:
        convert("9:60 AM to 5:60 PM")
    except ValueError:
        pass
    else:
        assert False, "Test failed: ValueError not raised for '9:60 AM to 5:60 PM'"

    try:
        convert("9 AM - 5 PM")
    except ValueError:
        pass
    else:
        assert False, "Test failed: ValueError not raised for '9 AM - 5 PM'"

    try:
        convert("9:00 AM - 5:00 PM")
    except ValueError:
        pass
    else:
        assert False, "Test failed: ValueError not raised for '9:00 AM - 5:00 PM'"

def test_output():
    # Valid inputs should give correct outputs
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00", "Hours conversion incorrect"
    assert convert("10:30 PM to 8:05 AM") == "22:30 to 08:05", "Minutes conversion incorrect"
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00", "Midnight/noon conversion incorrect"

if __name__ == "__main__":
    test_format()
    test_output()
    print("All tests passed.")
