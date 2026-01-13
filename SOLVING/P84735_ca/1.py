
import sys

case_num = 1
for line in sys.stdin:
    parts = line.split()
    if not parts:
        continue

    a, b = map(int, parts)

    if a % b == 0:
        result = a
    else:
        result = (a // b + 1) * b

    print(f"Case #{case_num}: {result}")
    case_num += 1
