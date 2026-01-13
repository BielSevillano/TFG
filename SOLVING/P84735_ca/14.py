
import sys

case_num = 1
for line in sys.stdin:
    try:
        a, b = map(int, line.split())

        # The remainder of the division of a by b.
        rem = a % b

        # If the remainder is 0, 'a' is already a multiple of 'b'.
        # Since we want the smallest multiple >= a, 'a' is the answer.
        if rem == 0:
            result = a
        # If there is a remainder, 'a' is not a multiple.
        # The next multiple of 'b' is 'a' plus the difference needed
        # to reach that multiple. This difference is (b - remainder).
        else:
            result = a + (b - rem)

        print(f"Case #{case_num}: {result}")
        case_num += 1
    except (ValueError, IndexError):
        # This handles potential empty or malformed lines in the input.
        # The loop will continue to the next line.
        pass
