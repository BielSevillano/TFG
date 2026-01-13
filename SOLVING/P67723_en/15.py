
import sys

def gcd(a, b):
    """
    Computes the greatest common divisor of two non-negative integers a and b
    using the Euclidean algorithm.
    """
    while b:
        a, b = b, a % b
    return a

def main():
    """
    Main function to read input, compute GCD, and print the result.
    It reads a single line containing two space-separated integers.
    """
    try:
        line = sys.stdin.readline()
        if line:
            a, b = map(int, line.split())
            # The problem statement guarantees a and b are strictly positive.
            result = gcd(a, b)
            print(result)
    except (ValueError, IndexError):
        # This handles potential malformed input, though not expected
        # based on the problem description.
        pass

if __name__ == "__main__":
    main()
