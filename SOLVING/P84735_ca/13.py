
import sys

case_num = 1
for line in sys.stdin:
    try:
        a, b = map(int, line.split())
    except ValueError:
        continue

    if a % b == 0:
        x = a
    else:
        # a = (a // b) * b + (a % b)
        # The next multiple of b is ((a // b) + 1) * b
        x = (a // b + 1) * b
        
    print(f"Case {case_num}: {x}")
    case_num += 1
