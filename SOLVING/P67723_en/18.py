
import sys

def gcd(a, b):
    """
    Computes the greatest common divisor of two non-negative integers
    using the Euclidean algorithm.
    """
    while b:
        a, b = b, a % b
    return a

try:
    # Read the two numbers from a single line of input.
    # Using sys.stdin.readline() for potential performance benefits in competitive programming.
    line = sys.stdin.readline()
    if line:
        a, b = map(int, line.split())
        
        # The problem statement guarantees strictly positive numbers,
        # so no need to check for a=0 or b=0 as initial input.
        
        # Compute and print the greatest common divisor.
        result = gcd(a, b)
        print(result)

except (IOError, ValueError):
    # This block handles potential empty input or malformed lines,
    # though the problem statement implies clean input.
    # It ensures the program exits gracefully.
    pass
