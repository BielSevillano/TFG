
import sys

def solve():
    """
    Reads pairs of numbers a, b and for each pair, prints the smallest
    natural number that is greater than or equal to a and also a multiple of b.
    """
    case_number = 1
    for line in sys.stdin:
        try:
            a, b = map(int, line.split())
        except (ValueError, IndexError):
            # Handles empty or malformed lines, though not expected in this problem.
            continue

        # If a is already a multiple of b, it is the smallest multiple >= a.
        if a % b == 0:
            result = a
        else:
            # Otherwise, the smallest multiple is the next one after (a // b) * b.
            # a // b gives the integer part of the division.
            # (a // b + 1) gives the multiplier for the next multiple of b.
            result = (a // b + 1) * b
        
        print(f"Case #{case_number}: {result}")
        case_number += 1

if __name__ == "__main__":
    solve()
