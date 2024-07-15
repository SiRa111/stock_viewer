from twttr import shorten


def test_lower():
  assert shorten("short word") == "shrt wrd"

def test_upper():
  assert shorten("UPPERCASE HUH") == "PPRCS HH"

def test_num():
  assert shorten("1234") == "1234"

def test_punc():
  assert shorten("hi!we:that.") == "h!w:tht"


