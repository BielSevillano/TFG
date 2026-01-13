
import sys

def gcd(a, b):
    """
    Computes the greatest common divisor of two numbers using the Euclidean algorithm.
    """
    while b:
        a, b = b, a % b
    return a

def main():
    """
    Reads pairs of numbers from standard input and prints their GCD.
    """
    for line in sys.stdin:
        try:
            # Split the line into two numbers and convert them to integers
            a, b = map(int, line.split())
            
            # Compute and print the GCD
            print(gcd(a, b))
        except (ValueError, IndexError):
            # This handles empty or malformed lines, making the program more robust.
            # For this specific problem, input is guaranteed to be correct,
            # but it's good practice.
            continue

if __name__ == "__main__":
    main()
