
import sys

case = 1
for line in sys.stdin:
    try:
        a, b = map(int, line.split())
    except ValueError:
        # This handles empty lines gracefully.
        continue

    # If 'a' is already a multiple of 'b', it is the smallest
    # multiple of 'b' that is greater than or equal to 'a'.
    if a % b == 0:
        x = a
    else:
        # Otherwise, the smallest multiple of 'b' greater than or equal to 'a'
        # is the next multiple after the one immediately preceding 'a'.
        # The multiple preceding or equal to 'a' is (a // b) * b.
        # The next multiple is ((a // b) + 1) * b.
        x = (a // b + 1) * b
        
    print(f"Case #{case}: {x}")
    case += 1
