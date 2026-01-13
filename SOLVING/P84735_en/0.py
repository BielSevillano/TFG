
import sys

def smallest_multiple():
    """
    Reads pairs of natural numbers a and b from standard input and for
    each one, prints the smallest natural number that is greater than or
    equal to a and also a multiple of b.
    """
    case_num = 1
    for line in sys.stdin:
        # Assuming input lines are not empty and correctly formatted
        try:
            a, b = map(int, line.split())
        except (ValueError, IndexError):
            # Handles potential empty lines or malformed input
            continue

        # If a is already a multiple of b, it is the smallest
        # multiple of b that is greater than or equal to a.
        remainder = a % b
        if remainder == 0:
            result = a
        else:
            # If a is not a multiple of b, the next multiple of b is
            # a - (remainder) + b. This finds the multiple of b just before a
            # (a - remainder) and then adds b to get the next one.
            result = a - remainder + b
        
        print(f"Case {case_num}: {result}")
        case_num += 1

if __name__ == "__main__":
    smallest_multiple()
