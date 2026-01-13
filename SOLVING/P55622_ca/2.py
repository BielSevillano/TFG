
import sys

# The input is a single natural number on a line.
# We can read the entire line as a string.
line = sys.stdin.readline()

# The number of digits is the length of the string,
# after removing any trailing whitespace like the newline character.
print(len(line.strip()))
