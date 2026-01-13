
import sys

def gcd(a, b):
    """Computes the greatest common divisor of a and b using the Euclidean algorithm."""
    while b:
        a, b = b, a % b
    return a

def main():
    """
    Reads pairs of numbers from standard input and prints their GCD.
    The loop continues until no more input is available.
    """
    for line in sys.stdin:
        # Process only non-empty lines
        if line.strip():
            try:
                a, b = map(int, line.split())
                # The problem statement guarantees strictly positive numbers.
                # No need to check for a > 0 and b > 0.
                print(gcd(a, b))
            except (ValueError, IndexError):
                # This block will be skipped for valid inputs as per the problem description.
                # It provides robustness against malformed lines.
                pass

if __name__ == "__main__":
    main()
