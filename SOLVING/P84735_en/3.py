
import sys

case_num = 1
for line in sys.stdin:
    try:
        a, b = map(int, line.split())

        # If a is already a multiple of b, it's the smallest multiple >= a.
        if a % b == 0:
            result = a
        # Otherwise, the smallest multiple >= a is the next multiple of b.
        # The integer division a // b gives the quotient.
        # The next multiple is (quotient + 1) * b.
        else:
            result = (a // b + 1) * b

        print(f'Case {case_num}: {result}')
        case_num += 1
    except ValueError:
        # This handles empty or malformed lines, which can occur at the
        # end of the input stream, causing map() or split() to fail.
        # We simply skip such lines.
        continue
