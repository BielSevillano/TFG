
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
    Reads two numbers from a single line of standard input,
    computes their GCD, and prints the result.
    """
    try:
        # Read a single line from standard input.
        line = sys.stdin.readline()
        
        # Check if the line is not empty (to handle end-of-file).
        if line:
            # Split the line by whitespace and convert parts to integers.
            a, b = map(int, line.split())
            
            # Compute the greatest common divisor.
            result = gcd(a, b)
            
            # Print the result to standard output.
            print(result)
            
    except (ValueError, IndexError):
        # This block will handle cases with malformed input,
        # such as non-integer values or an incorrect number of values.
        # For this problem, assuming valid input, it's a safeguard.
        pass

if __name__ == "__main__":
    main()
