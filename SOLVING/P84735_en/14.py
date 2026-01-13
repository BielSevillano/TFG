
import sys

case_num = 1
for line in sys.stdin:
    try:
        a, b = map(int, line.split())

        # If a is already a multiple of b, it is the smallest multiple >= a.
        if a % b == 0:
            x = a
        else:
            # Otherwise, the smallest multiple is the next one.
            # We find the quotient of the integer division, add 1,
            # and multiply by b.
            x = (a // b + 1) * b

        print(f"Case {case_num}: {x}")
        case_num += 1
    except (ValueError, IndexError):
        # This handles cases where a line is empty or malformed,
        # typically indicating the end of input.
        break
