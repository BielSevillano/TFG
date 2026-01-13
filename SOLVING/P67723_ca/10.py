
import sys

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

for line in sys.stdin:
    try:
        a, b = map(int, line.split())
        print(gcd(a, b))
    except (ValueError, IndexError):
        continue
