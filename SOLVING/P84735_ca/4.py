
import sys

def solve():
    """
    Reads pairs of natural numbers a and b and for each pair,
    prints the smallest natural number x such that x >= a and x is a multiple of b.
    """
    case_number = 1
    for line in sys.stdin:
        # Assuming each line is well-formed with two integers separated by space.
        # The loop will terminate automatically at the end of the input (EOF).
        try:
            a, b = map(int, line.split())
        except (ValueError, IndexError):
            # Skip empty or malformed lines if they occur
            continue

        # If a is already a multiple of b, it is the smallest multiple >= a.
        if a % b == 0:
            result = a
        else:
            # If a is not a multiple of b, we need to find the next one.
            # a // b gives the integer quotient.
            # (a // b) * b is the largest multiple of b that is <= a.
            # The next multiple is therefore (a // b + 1) * b.
            result = (a // b + 1) * b

        # Print the output in the required format.
        print(f"Case #{case_number}: {result}")
        case_number += 1

solve()
