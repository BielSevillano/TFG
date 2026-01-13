
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
    Main function to read input and print the result.
    """
    try:
        # Read the entire input at once in case there are multiple lines,
        # though the problem implies a single line.
        input_data = sys.stdin.read()
        # Split into words and convert to integers.
        numbers = list(map(int, input_data.split()))
        
        if len(numbers) >= 2:
            a = numbers[0]
            b = numbers[1]
            
            # The problem states strictly positive numbers,
            # so we don't need to handle zero or negative cases.
            result = gcd(a, b)
            print(result)
            
    except (ValueError, IndexError):
        # This block will handle cases with malformed input,
        # although it's not expected based on the problem description.
        pass

if __name__ == "__main__":
    main()
