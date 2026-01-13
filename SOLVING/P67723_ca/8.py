
import sys

def gcd(a, b):
    """
    Calculates the greatest common divisor of two numbers a and b
    using the Euclidean algorithm.
    """
    while b:
        a, b = b, a % b
    return a

def main():
    """
    Main function to read input and print the result.
    It reads a single line containing two numbers.
    """
    try:
        # Read the entire line to handle potential multiple test cases per run,
        # though the problem statement implies a single case.
        # This approach is robust for various input scenarios.
        line = sys.stdin.readline()
        if not line:
            return

        # Split the line and convert to integers
        a, b = map(int, line.split())

        # Calculate and print the GCD
        result = gcd(a, b)
        print(result)

    except (ValueError, IndexError):
        # In case of malformed input, gracefully exit.
        # Jutge.org typically provides well-formed input.
        pass

if __name__ == "__main__":
    main()
