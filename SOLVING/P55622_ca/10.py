
import sys

# Since the input is guaranteed to be a natural number,
# we can read it as a string and its length will be the number of digits.
# This handles the case n=0 correctly (len("0") is 1).
# It's also generally faster in Python for this specific problem than
# mathematical or iterative methods, especially with large numbers.
n_str = sys.stdin.readline().strip()
print(len(n_str))
