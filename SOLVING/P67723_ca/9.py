
import sys

def gcd(a, b):
    """
    Calculates the greatest common divisor of a and b using the Euclidean algorithm.
    """
    while b:
        a, b = b, a % b
    return a

def main():
    """
    Reads pairs of numbers from standard input and prints their GCD.
    """
    for line in sys.stdin:
        # Strip the line to handle potential trailing whitespace and check if it's not empty
        line = line.strip()
        if line:
            try:
                a, b = map(int, line.split())
                print(gcd(a, b))
            except (ValueError, IndexError):
                # In case of malformed lines, though not expected by problem spec
                continue

if __name__ == "__main__":
    main()
