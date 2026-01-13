
import sys

def solve():
    """
    Reads pairs of natural numbers a and b from standard input and for each
    pair, prints the smallest natural number x such that x >= a and x is a
    multiple of b.
    """
    case_number = 1
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue

        try:
            a, b = map(int, line.split())
        except (ValueError, IndexError):
            # Skip malformed lines
            continue

        # If a is already a multiple of b, it is the smallest multiple >= a.
        if a % b == 0:
            result = a
        else:
            # Otherwise, find the multiple of b just before a, which is
            # (a // b) * b, and the next multiple is what we want.
            result = (a // b + 1) * b

        print(f"Case #{case_number}: {result}")
        case_number += 1

if __name__ == "__main__":
    solve()
