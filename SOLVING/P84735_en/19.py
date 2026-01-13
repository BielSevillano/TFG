
import sys

case_number = 1
for line in sys.stdin:
    # Read a pair of natural numbers a and b from a line.
    # The split() method handles any amount of whitespace between numbers.
    try:
        a, b = map(int, line.split())
    except (ValueError, IndexError):
        # This handles empty or malformed lines, if any.
        continue

    # We are looking for the smallest natural number x such that:
    # 1. x >= a
    # 2. x is a multiple of b (i.e., x % b == 0)

    # Case 1: 'a' is already a multiple of b.
    # In this case, 'a' itself is the smallest number that meets both conditions.
    if a % b == 0:
        result = a
    # Case 2: 'a' is not a multiple of b.
    # We need to find the first multiple of b that is greater than a.
    # Integer division (a // b) gives the quotient q, such that q * b <= a.
    # The next multiple of b is (q + 1) * b, which will be >= a.
    else:
        result = (a // b + 1) * b

    # Print the output in the specified format.
    print(f"Case #{case_number}: {result}")
    case_number += 1
