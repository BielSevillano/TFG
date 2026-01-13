
import sys

def main():
    """
    Reads pairs of numbers a, b and for each pair, prints the smallest
    multiple of b that is greater than or equal to a.
    """
    case_num = 1
    for line in sys.stdin:
        # Split the line into parts. Handles lines with trailing/leading spaces.
        # If a line is empty or just whitespace, parts will be an empty list.
        parts = line.split()
        if not parts:
            continue

        a, b = map(int, parts)

        # The problem guarantees b >= 1, so we don't need to check for b=0.

        # If a is already a multiple of b, it is the smallest multiple of b
        # that is greater than or equal to a.
        if a % b == 0:
            result = a
        else:
            # If a is not a multiple of b, we need to find the next higher multiple.
            # Integer division (a // b) gives the number of full times b fits into a.
            # So, (a // b) * b is the largest multiple of b that is <= a.
            # The next multiple is what we want.
            result = (a // b + 1) * b
        
        print(f"Case {case_num}: {result}")
        case_num += 1

if __name__ == "__main__":
    main()
