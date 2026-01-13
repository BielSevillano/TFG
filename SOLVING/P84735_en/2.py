
import sys

def solve():
    """
    Reads pairs of natural numbers a and b from stdin and for each pair,
    prints the smallest natural number >= a that is a multiple of b.
    """
    case_number = 1
    for line in sys.stdin:
        try:
            # Read a and b from the current line
            a, b = map(int, line.split())
        except (ValueError, IndexError):
            # Skip empty or malformed lines
            continue

        # If a is already a multiple of b, it is the smallest multiple
        # greater than or equal to itself.
        if a % b == 0:
            result = a
        else:
            # Otherwise, the smallest multiple greater than a is the next
            # multiple of b. We find the multiple of b just before a
            # (which is (a // b) * b) and add b to get to the next one.
            result = (a // b + 1) * b

        # Print the result in the required format
        print(f"Case #{case_number}: {result}")
        case_number += 1

if __name__ == "__main__":
    solve()
