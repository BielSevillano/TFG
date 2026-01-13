
import sys

# The problem states that the input is a single natural number.
# We read one line from the standard input, which will contain this number.
line = sys.stdin.readline()

# The number of digits of a number is simply the length of its string representation.
# We use .strip() to remove any leading/trailing whitespace, including the
# trailing newline character that sys.stdin.readline() captures.
num_str = line.strip()

# We print the length of the resulting string.
print(len(num_str))
