
import sys

def gcd(a, b):
    """
    Computes the greatest common divisor of two positive integers
    using the Euclidean algorithm.
    """
    while b:
        a, b = b, a % b
    return a

def main():
    """
    Main function to read input and solve the problem.
    It reads a single line containing two numbers, computes their GCD,
    and prints the result.
    """
    # The problem statement implies a single line of input.
    # We read from sys.stdin to handle input redirection.
    line = sys.stdin.readline()
    
    # Ensure the line is not empty (handles EOF)
    if line:
        try:
            # Split the line and convert the two parts to integers
            a, b = map(int, line.split())
            
            # Compute and print the GCD
            result = gcd(a, b)
            print(result)
        except (ValueError, IndexError):
            # This handles cases of malformed input, although the problem
            # description implies valid input will be provided.
            pass

if __name__ == "__main__":
    main()
