
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
    Reads pairs of numbers from standard input until EOF and prints their GCD.
    """
    for line in sys.stdin:
        try:
            # Split the line and convert parts to integers
            a, b = map(int, line.split())
            
            # The problem states strictly positive numbers, so no need to check for a=0 or b=0
            # as the base case for the algorithm. The algorithm handles it anyway.
            
            # Compute and print the GCD
            result = gcd(a, b)
            print(result)
        except (ValueError, IndexError):
            # This handles cases where a line might be empty or malformed.
            # For well-formed input as per the problem, this might not be strictly necessary.
            continue

if __name__ == "__main__":
    main()
