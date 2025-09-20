import re

def convert(s):
    # Regex with anchors and strict matching
    pattern = r"^([1-9]|1[0-2]):?([0-5]\d)? (AM|PM) to ([1-9]|1[0-2]):?([0-5]\d)? (AM|PM)$"
    match = re.match(pattern, s)
    if not match:
        raise ValueError("Invalid time format")

    h1, m1, p1, h2, m2, p2 = match.groups()

    # Default minutes to "00" if missing
    m1 = m1 if m1 else "00"
    m2 = m2 if m2 else "00"

    h1 = int(h1)
    h2 = int(h2)
    m1 = int(m1)
    m2 = int(m2)

    # Validate ranges
    if not (1 <= h1 <= 12) or not (1 <= h2 <= 12):
        raise ValueError("Invalid hour")
    if not (0 <= m1 < 60) or not (0 <= m2 < 60):
        raise ValueError("Invalid minute")

    # Convert to 24-hour format
    h1 = to_24(h1, p1)
    h2 = to_24(h2, p2)

    return f"{h1:02}:{m1:02} to {h2:02}:{m2:02}"


def to_24(hour, period):
    if period == "AM":
        if hour == 12:
            return 0
        return hour
    elif period == "PM":
        if hour != 12:
            return hour + 12
        return hour
    else:
        raise ValueError("Invalid period")


if __name__ == "__main__":
    print(convert(input("Hours: ")))
