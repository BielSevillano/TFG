
import sys

def gcd(a, b):
    """
    Computes the greatest common divisor of a and b using the Euclidean algorithm.
    """
    while b:
        a, b = b, a % b
    return a

def main():
    """
    Reads pairs of numbers from standard input, one pair per line,
    and prints their greatest common divisor.
    """
    for line in sys.stdin:
        # Skip empty lines which could be present in the input
        if line.strip():
            try:
                a, b = map(int, line.split())
                result = gcd(a, b)
                print(result)
            except (ValueError, IndexError):
                # In case of malformed lines, just ignore them and continue.
                # The problem statement implies valid input, but this adds robustness.
                pass

if __name__ == "__main__":
    main()
