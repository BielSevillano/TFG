
import sys

try:
    line = sys.stdin.readline().strip()
    if line:
        n = int(line)
        if n == 0:
            print(1)
        else:
            count = 0
            while n > 0:
                n //= 10
                count += 1
            print(count)
except (ValueError, IndexError):
    pass
