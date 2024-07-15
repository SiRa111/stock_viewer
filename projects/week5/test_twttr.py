from twttr import shorten

def test_lower():
  assert shorten("short word") == "shrt wrd"

def test_upper():
  assert shorten("UPPERCASE HUH") == "PPRCSE HH"

def test_num():
  
