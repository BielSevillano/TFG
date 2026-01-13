
import sys

def gcd(a, b):
    """
    Computes the greatest common divisor of two non-negative integers
    using the Euclidean algorithm.
    """
    while b:
        a, b = b, a % b
    return a

def main():
    """
    Reads pairs of numbers from standard input and prints their GCD.
    """
    for line in sys.stdin:
        # Strip whitespace from the beginning and end of the line
        line = line.strip()
        # Process the line only if it's not empty
        if line:
            try:
                # Split the line by whitespace, convert parts to integers
                num1, num2 = map(int, line.split())
                # Compute and print the greatest common divisor
                print(gcd(num1, num2))
            except (ValueError, IndexError):
                # This handles lines that do not contain two valid integers.
                # For this problem, input is guaranteed to be correct,
                # but this makes the code more robust.
                continue

if __name__ == "__main__":
    main()
