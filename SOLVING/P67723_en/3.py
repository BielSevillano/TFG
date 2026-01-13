
import sys

def gcd(a, b):
    """
    Computes the greatest common divisor of two numbers using the Euclidean algorithm.
    """
    while b:
        a, b = b, a % b
    return a

def main():
    """
    Reads pairs of numbers from standard input until EOF
    and prints their greatest common divisor.
    """
    for line in sys.stdin:
        try:
            # Split the line and convert parts to integers
            a, b = map(int, line.split())
            
            # Compute and print the GCD
            print(gcd(a, b))
            
        except (ValueError, IndexError):
            # Skip empty or malformed lines
            continue

if __name__ == "__main__":
    main()
