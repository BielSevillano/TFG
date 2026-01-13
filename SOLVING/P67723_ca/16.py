
import sys

def gcd(a, b):
    """
    Calculates the greatest common divisor of two positive integers
    using the Euclidean algorithm.
    """
    while b:
        a, b = b, a % b
    return a

def main():
    """
    Reads two integers from standard input and prints their GCD.
    """
    # The problem implies a single line of input with two numbers.
    # Reading once is sufficient.
    try:
        line = sys.stdin.readline()
        if line:
            a, b = map(int, line.split())
            print(gcd(a, b))
    except (ValueError, IndexError):
        # This handles potential empty lines or malformed input,
        # although problem constraints usually prevent this.
        pass

if __name__ == "__main__":
    main()
