
import sys

# The input is a single line containing a natural number.
# We can read it as a string and its length will be the number of digits.
# This is efficient and handles the edge case of 0 correctly.
line = sys.stdin.readline().strip()

# If the line is not empty (to handle potential empty input gracefully,
# although the problem statement implies a valid natural number)
if line:
    print(len(line))

