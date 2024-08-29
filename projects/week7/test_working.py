from working import convert

def test_format(v):
    with v.assertRaises(ValueError):
        convert("9:60 AM to 5:60 PM")
    with v.assertRaises(ValueError):
        convert("9 AM - 5 PM ")
    with v.assertRaises(ValueError):
        convert("9:00 AM - 5:00 PM") 

