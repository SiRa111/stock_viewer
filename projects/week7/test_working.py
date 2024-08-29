from working import convert  # Replace 'working' with the actual name of your script

def test_format():
    # Test 1: Invalid minutes
    try:
        convert("9:60 AM to 5:60 PM")
    except ValueError:
        pass  # Test passed
    else:
        assert False, "Test failed: ValueError not raised for '9:60 AM to 5:60 PM'"

    # Test 2: Incorrect time separator
    try:
        convert("9 AM - 5 PM")
    except ValueError:
        pass  # Test passed
    else:
        assert False, "Test failed: ValueError not raised for '9 AM - 5 PM'"

    # Test 3: Incorrect format
    try:
        convert("9:00 AM - 5:00 PM")
    except ValueError:
        pass  # Test passed
    else:
        assert False, "Test failed: ValueError not raised for '9:00 AM - 5:00 PM'"

if __name__ == "__main__":
    test_format()
    print("All tests passed.")
