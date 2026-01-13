
import sys

try:
    n_str = input()
    n = int(n_str)
    print(len(str(n)))
except (IOError, ValueError):
    # This part handles potential empty input or non-integer input,
    # although problem constraints usually guarantee valid input.
    # For the specific case of n=0, int("0") is 0, str(0) is "0", len is 1, which is correct.
    # If input is empty, a ValueError or EOFError would be raised by input() or int().
    # In a typical Jutge environment, an empty input should not occur for this problem.
    # If it did, exiting gracefully is a reasonable behavior.
    pass
