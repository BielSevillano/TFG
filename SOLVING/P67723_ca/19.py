
import sys

def gcd(a, b):
    """
    Calculates the greatest common divisor of two numbers using the Euclidean algorithm.
    """
    while b:
        a, b = b, a % b
    return a

def main():
    """
    Reads pairs of numbers from standard input and prints their GCD.
    """
    for line in sys.stdin:
        # Strip the line to handle potential trailing whitespace and check if it's empty
        line = line.strip()
        if not line:
            continue
        
        try:
            # Split the line into two numbers and convert them to integers
            a, b = map(int, line.split())
            
            # Calculate and print the GCD
            result = gcd(a, b)
            print(result)
            
        except (ValueError, IndexError):
            # If a line is malformed (e.g., not two numbers), skip it.
            continue

if __name__ == "__main__":
    main()
