
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
    Reads pairs of numbers from standard input and prints their GCD.
    """
    for line in sys.stdin:
        try:
            # Split the line and convert to two integers
            a, b = map(int, line.split())
            # Calculate and print the GCD
            print(gcd(a, b))
        except ValueError:
            # This handles cases where the line is empty or doesn't contain two integers,
            # allowing the program to continue to the next line or terminate gracefully.
            continue

if __name__ == "__main__":
    main()
