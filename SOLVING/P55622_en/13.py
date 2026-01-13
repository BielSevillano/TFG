
import sys

for line in sys.stdin:
    # Each line contains a number. We strip leading/trailing whitespace,
    # including the newline character at the end of the line.
    number_as_string = line.strip()

    # The problem guarantees a natural number, so we don't expect empty lines.
    # However, checking for non-empty strings is a robust practice.
    if number_as_string:
        # The number of digits is simply the length of the string.
        print(len(number_as_string))
