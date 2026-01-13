
import sys

case_num = 1
for line in sys.stdin:
    try:
        a, b = map(int, line.split())
    except ValueError:
        # This handles empty or malformed lines, if any
        continue

    # We are looking for the smallest multiple of b, let's call it x,
    # such that x is greater than or equal to a.

    # If a is already a multiple of b, then a itself is the answer,
    # because it's the smallest number >= a that is a multiple of b.
    if a % b == 0:
        result = a
    else:
        # If a is not a multiple of b, we need to find the next multiple.
        # Integer division a // b gives the quotient, which corresponds to
        # the multiple of b just before or at a.
        # (a // b) * b is the largest multiple of b less than or equal to a.
        # The next multiple is found by adding 1 to the quotient.
        result = (a // b + 1) * b

    print(f"Case {case_num}: {result}")
    case_num += 1
