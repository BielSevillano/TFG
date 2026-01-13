
import sys

def solve():
    """
    Reads pairs of natural numbers a and b from stdin, and for each pair,
    prints the smallest natural number x such that x >= a and x is a multiple of b.
    """
    case_number = 1
    for line in sys.stdin:
        # Assuming input lines are well-formed with two integers.
        # An empty line would cause a ValueError here, which would terminate
        # the program if not handled, but usually input is clean.
        try:
            a, b = map(int, line.split())
        except (ValueError, IndexError):
            # This handles empty lines or malformed input gracefully
            # and stops the loop, which is appropriate for EOF.
            break

        # If a is already a multiple of b, it is the smallest number >= a
        # that satisfies the condition.
        if a % b == 0:
            result = a
        else:
            # If a is not a multiple of b, the smallest multiple of b >= a
            # is the one that comes immediately after the largest multiple of b < a.
            # The largest multiple of b <= a is (a // b) * b.
            # The next one is (a // b + 1) * b.
            result = (a // b + 1) * b

        # Print the output in the required format.
        print(f"Case #{case_number}: {result}")
        case_number += 1

solve()
