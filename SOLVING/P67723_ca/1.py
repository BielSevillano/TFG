
import sys

def gcd(a, b):
    """
    Calculates the greatest common divisor of two numbers
    using the Euclidean algorithm.
    """
    while b:
        a, b = b, a % b
    return a

def main():
    """
    Main function to read input and print the GCD.
    """
    try:
        # Read the two numbers from a single line of input.
        # Jutge.org typically provides input on a single line for this kind of problem.
        line = sys.stdin.readline()
        if line:
            a, b = map(int, line.split())
            
            # Calculate and print the result.
            result = gcd(a, b)
            print(result)
            
    except (ValueError, IndexError):
        # This handles cases with malformed input, although Jutge.org
        # usually guarantees the input format.
        pass

if __name__ == "__main__":
    main()
