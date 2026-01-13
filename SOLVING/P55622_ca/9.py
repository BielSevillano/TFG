
import sys

# Reading the number as a string is the most direct approach.
# The problem guarantees the input is a natural number, so the
# string will consist of one or more digit characters.
try:
    n_str = input()
    # The number of digits is simply the length of its string representation.
    # This correctly handles the edge case of n = 0, where len("0") is 1.
    print(len(n_str))
except EOFError:
    # This handles the case of empty input, although the problem
    # statement implies there will always be one number.
    pass
