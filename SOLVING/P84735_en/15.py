
import sys

def main():
    """
    Reads pairs of natural numbers a and b, and for each one
    prints the smallest natural number >= a that is a multiple of b.
    """
    case_number = 1
    for line in sys.stdin:
        try:
            # Split the line and convert to integers
            a, b = map(int, line.split())
        except (ValueError, IndexError):
            # Skip empty or malformed lines
            continue

        # If a is already a multiple of b, it is the smallest multiple >= a.
        if a % b == 0:
            result = a
        else:
            # Otherwise, we need to find the next multiple of b.
            # The quotient of the division is a // b.
            # (a // b) * b is the largest multiple of b that is <= a.
            # So, the next multiple is ((a // b) + 1) * b.
            result = (a // b + 1) * b

        print(f"Case #{case_number}: {result}")
        case_number += 1

if __name__ == "__main__":
    main()
