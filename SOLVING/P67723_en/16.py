
import sys

def gcd(a, b):
    """
    Computes the greatest common divisor of two non-negative integers a and b
    using the Euclidean algorithm.
    """
    while b:
        a, b = b, a % b
    return a

def main():
    """
    Reads two integers from a single line of standard input,
    calculates their greatest common divisor, and prints the result.
    """
    try:
        # Read a single line from input
        line = sys.stdin.readline()
        # If the line is empty, we've reached the end of input
        if not line:
            return

        # Split the line into numbers and convert them to integers
        a, b = map(int, line.split())

        # Calculate and print the GCD
        result = gcd(a, b)
        print(result)

    except (ValueError, IndexError):
        # This handles potential empty lines or malformed input,
        # although the problem statement implies valid input.
        pass

if __name__ == "__main__":
    main()
