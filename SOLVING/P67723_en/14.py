
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
    Reads pairs of numbers from standard input and prints their GCD.
    The loop terminates when there is no more input.
    """
    for line in sys.stdin:
        # Strip whitespace from the line and check if it's not empty
        line = line.strip()
        if not line:
            continue
        
        try:
            # Split the line into two numbers and convert them to integers
            a, b = map(int, line.split())
            
            # The problem specifies strictly positive numbers
            if a > 0 and b > 0:
                # Calculate and print the GCD
                result = gcd(a, b)
                print(result)

        except (ValueError, IndexError):
            # If a line is malformed (e.g., not two numbers),
            # skip it and continue with the next line.
            continue

if __name__ == "__main__":
    main()
