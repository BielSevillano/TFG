
import sys

def solve():
    """
    Reads pairs of natural numbers a and b from standard input and for each pair,
    writes the smallest natural number x such that x >= a and x is a multiple of b.
    """
    case_num = 1
    for line in sys.stdin:
        # Strip whitespace and check for empty lines
        line = line.strip()
        if not line:
            continue

        try:
            a, b = map(int, line.split())
        except (ValueError, IndexError):
            # Skip malformed lines
            continue

        # The problem guarantees b >= 1.

        # If a is already a multiple of b, then a is the answer.
        if a % b == 0:
            result = a
        else:
            # Otherwise, the answer is the next multiple of b.
            # The integer division a // b gives the quotient of a divided by b.
            # (a // b) * b is the largest multiple of b less than or equal to a.
            # Since a is not a multiple, this is strictly less than a.
            # The next multiple is obtained by adding 1 to the quotient.
            result = (a // b + 1) * b

        # Print the result in the specified format "Cas #N: result"
        print(f"Cas #{case_num}: {result}")
        case_num += 1

solve()
