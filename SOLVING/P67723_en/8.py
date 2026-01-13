
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
    Reads pairs of numbers from standard input and prints their GCD for each pair.
    """
    for line in sys.stdin:
        # Skips empty lines that might be present in the input
        if not line.strip():
            continue
        try:
            a, b = map(int, line.split())
            # Problem states numbers are strictly positive, but the algorithm works
            # for non-negative integers as well.
            result = gcd(a, b)
            print(result)
        except (ValueError, IndexError):
            # In case of malformed lines (e.g., non-integers, wrong number of values),
            # this robustly skips them.
            pass

if __name__ == "__main__":
    main()
