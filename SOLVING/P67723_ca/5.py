
import sys

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

for line in sys.stdin:
    try:
        a, b = map(int, line.split())
        result = gcd(a, b)
        print(result)
    except (ValueError, IndexError):
        # In case of empty lines or other format errors, just continue
        pass
