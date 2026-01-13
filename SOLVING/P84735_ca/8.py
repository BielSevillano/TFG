
import sys

case_count = 1
for line in sys.stdin:
    parts = line.split()
    if not parts:
        continue

    try:
        a, b = map(int, parts)

        if a % b == 0:
            result = a
        else:
            result = (a // b + 1) * b

        print(f"Case #{case_count}: {result}")
        case_count += 1
    except (ValueError, IndexError):
        # This handles potential malformed lines or empty lines at the end of input
        # and allows the program to terminate gracefully.
        break
