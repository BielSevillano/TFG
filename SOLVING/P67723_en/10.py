
import sys

def gcd(a, b):
    """
    Computes the greatest common divisor of two numbers using the Euclidean algorithm.
    """
    while b:
        a, b = b, a % b
    return a

for line in sys.stdin:
    try:
        a, b = map(int, line.split())
        if a > 0 and b > 0:
            result = gcd(a, b)
            print(result)
    except (ValueError, IndexError):
        # This handles empty or malformed lines without crashing.
        # The loop will simply continue to the next line or terminate if it's the end of input.
        pass
