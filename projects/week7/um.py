import re
import sys


def main():
    text = input("Text: ")
    print(count(text))


def count(s: str) -> int:
    """
    Count occurrences of 'um' in the string s,
    case-insensitive, as a standalone word.
    """
    matches = re.findall(r"\bum\b", s, re.IGNORECASE)
    return len(matches)


if __name__ == "__main__":
    main()
