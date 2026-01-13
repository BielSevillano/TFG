
import sys

def main():
    """
    Reads pairs of natural numbers a and b from standard input, and for
    each pair, prints the smallest natural number that is greater than or
    equal to a and also a multiple of b.
    """
    case_number = 1
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue

        try:
            a, b = map(int, line.split())
        except (ValueError, IndexError):
            # Skip malformed lines, if any.
            continue

        # The task is to find the smallest multiple of b, let's call it x,
        # such that x >= a.
        # This is equivalent to finding the ceiling of a/b and multiplying by b.
        # Let's say x = m * b. We need m * b >= a, so m >= a / b.
        # The smallest integer m satisfying this is ceil(a/b).
        #
        # In integer arithmetic, ceil(a/b) can be calculated in a few ways.

        # Method 1: Using the modulo operator (very clear)
        if a % b == 0:
            # If a is already a multiple of b, it's the smallest >= a.
            result = a
        else:
            # Otherwise, we need the next multiple of b.
            # a // b is the integer quotient. The next multiple is (quotient + 1) * b.
            result = (a // b + 1) * b
        
        # Method 2: A compact branchless formula (often slightly faster)
        # result = ((a + b - 1) // b) * b
        # This formula is a standard way to compute ceil(a/b) * b with integers.

        print(f"Case #{case_number}: {result}")
        case_number += 1

if __name__ == "__main__":
    main()
