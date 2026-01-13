
import sys

def main():
    """
    Reads pairs of natural numbers a and b from standard input.
    For each pair, it calculates and prints the smallest natural number x
    such that x >= a and x is a multiple of b.
    """
    case_number = 1
    for line in sys.stdin:
        # Strip whitespace and check for empty lines
        line = line.strip()
        if not line:
            continue

        try:
            a, b = map(int, line.split())
        except (ValueError, IndexError):
            # Skip malformed lines, though not expected by the problem statement
            continue

        # Problem statement guarantees b >= 1.

        # If a is already a multiple of b, then a is the answer.
        if a % b == 0:
            result = a
        else:
            # Otherwise, the answer is the next multiple of b.
            # a = (quotient * b) + remainder
            # quotient = a // b
            # The next multiple is (quotient + 1) * b
            result = (a // b + 1) * b
        
        print(f"Case #{case_number}: {result}")
        case_number += 1

if __name__ == "__main__":
    main()
