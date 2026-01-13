
import sys

def main():
    """
    Reads pairs of natural numbers a, b from stdin and for each pair,
    prints the smallest natural number x such that x >= a and x is a multiple of b.
    """
    case_number = 1
    for line in sys.stdin:
        # Strip potential leading/trailing whitespace and check for empty lines
        line = line.strip()
        if not line:
            continue

        # Parse the two numbers
        try:
            a, b = map(int, line.split())
        except (ValueError, IndexError):
            # Skip malformed lines
            continue

        # If a is already a multiple of b, it's the answer.
        if a % b == 0:
            result = a
        else:
            # Otherwise, we need the next multiple of b.
            # a // b gives the integer quotient.
            # (a // b) * b is the largest multiple of b less than or equal to a.
            # The next multiple is therefore (a // b + 1) * b.
            result = (a // b + 1) * b

        # Print the output in the specified format
        print(f"Case {case_number}: {result}")
        case_number += 1

if __name__ == "__main__":
    main()
