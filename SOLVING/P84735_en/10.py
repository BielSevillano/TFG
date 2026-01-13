
import sys

case_counter = 1
for line in sys.stdin:
    try:
        a, b = map(int, line.split())
    except (ValueError, IndexError):
        # This handles empty or malformed lines, allowing the program to terminate gracefully.
        continue

    # If 'a' is already a multiple of 'b', it is the smallest multiple
    # greater than or equal to 'a'.
    if a % b == 0:
        result = a
    else:
        # Otherwise, the smallest multiple of 'b' greater than 'a' is
        # the next multiple after the one just before 'a'.
        # The multiple just before or at 'a' is (a // b) * b.
        # The next multiple is (a // b + 1) * b.
        result = (a // b + 1) * b

    print(f"Case #{case_counter}: {result}")
    case_counter += 1
