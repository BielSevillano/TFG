
import sys

def solve():
    """
    Reads pairs of natural numbers a and b, and for each one prints
    the smallest natural number that is greater than or equal to a
    and also a multiple of b.
    """
    case_number = 1
    for line in sys.stdin:
        # The input stream might contain empty lines, especially at the end.
        # We strip the line and check if it's empty to avoid errors.
        stripped_line = line.strip()
        if not stripped_line:
            continue

        a, b = map(int, stripped_line.split())

        # If 'a' is already a multiple of 'b', then 'a' is the answer.
        if a % b == 0:
            result = a
        else:
            # If 'a' is not a multiple of 'b', we need to find the next
            # multiple of 'b'.
            # (a // b) gives how many times 'b' fits completely into 'a'.
            # So, (a // b) * b is the largest multiple of 'b' that is <= a.
            # The next multiple of 'b' is found by adding 'b' to this,
            # or equivalently, by taking the next integer multiplier.
            result = (a // b + 1) * b

        print(f"Case #{case_number}: {result}")
        case_number += 1

solve()
