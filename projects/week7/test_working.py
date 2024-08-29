from working import convert  

def test_format():

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

    orrect format
    try:
        convert("9:00 AM - 5:00 PM")
    except ValueError:
        pass
    else:
        assert False, "Test failed: ValueError not raised for '9:00 AM - 5:00 PM'"

if __name__ == "__main__":
    test_format()
    print("All tests passed.")
