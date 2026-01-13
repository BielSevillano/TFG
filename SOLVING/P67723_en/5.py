
import sys

def gcd(a, b):
    """Computes the greatest common divisor of two numbers using the Euclidean algorithm."""
    while b:
        a, b = b, a % b
    return a

def main():
    """Main function to read input and print the GCD."""
    # It's good practice to handle multiple lines of input in competitive programming,
    # even if the problem statement implies a single line.
    # Reading line by line from stdin is a robust way.
    for line in sys.stdin:
        try:
            # Split the line into numbers and convert them to integers
            a, b = map(int, line.split())
            
            # Compute the GCD and print the result
            print(gcd(a, b))
        except (ValueError, IndexError):
            # In case of empty or malformed lines, just continue or break.
            # For this problem, we can assume valid input and could omit this,
            # but it makes the code more robust.
            pass

if __name__ == "__main__":
    main()
