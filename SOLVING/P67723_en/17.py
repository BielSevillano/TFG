
import sys

def gcd(a, b):
    """
    Computes the greatest common divisor of two numbers a and b
    using the Euclidean algorithm.
    """
    while b:
        a, b = b, a % b
    return a

def main():
    """
    Reads pairs of numbers from standard input and prints their GCD.
    The loop continues until the end of the input stream.
    """
    for line in sys.stdin:
        # A try-except block handles potential empty lines at the end of input
        # or malformed lines, preventing the program from crashing.
        try:
            # Split the line by whitespace, convert parts to integers
            a, b = map(int, line.split())
            # Calculate and print the greatest common divisor
            result = gcd(a, b)
            print(result)
        except ValueError:
            # If a line is empty or cannot be converted to two integers,
            # just continue to the next line.
            continue

if __name__ == "__main__":
    main()
