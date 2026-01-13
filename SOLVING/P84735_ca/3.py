
import sys

case = 1
for line in sys.stdin:
    try:
        a, b = map(int, line.split())
    except (ValueError, IndexError):
        continue

    # If a is already a multiple of b, it is the smallest number
    # greater than or equal to a that is a multiple of b.
    if a % b == 0:
        x = a
    else:
        # Otherwise, the answer is the next multiple of b.
        # We find the largest multiple of b less than a, which is (a // b) * b,
        # and then add b to get the next one.
        x = (a // b + 1) * b

    print(f"Case #{case}: {x}")
    case += 1
