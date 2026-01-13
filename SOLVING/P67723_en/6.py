
import sys

def gcd(a, b):
    """
    Computes the greatest common divisor of a and b using the Euclidean algorithm.
    """
    while b:
        a, b = b, a % b
    return a

def main():
    """
    Reads pairs of numbers from standard input and prints their GCD.
    This handles multiple lines of input, processing each as a separate case.
    """
    for line in sys.stdin:
        # Split the line by whitespace. If the line is empty or contains only
        # whitespace, 'parts' will be an empty list.
        parts = line.split()
        
        # Proceed only if the line was not empty.
        if parts:
            try:
                # Convert the parts to integers. We assume two numbers per line.
                num1, num2 = map(int, parts)
                
                # Calculate the GCD and print the result.
                print(gcd(num1, num2))
            except (ValueError, IndexError):
                # Ignore malformed lines and continue to the next.
                pass

if __name__ == "__main__":
    main()
