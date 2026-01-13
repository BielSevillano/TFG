
import sys

def gcd(a, b):
    """
    Calculates the greatest common divisor of two non-negative integers
    using the Euclidean algorithm.
    """
    while b:
        a, b = b, a % b
    return a

# It's common in competitive programming to read all lines until EOF.
# This loop structure handles that pattern robustly.
for line in sys.stdin:
    # Ensure the line is not empty or just whitespace
    if line.strip():
        try:
            # Split the line into parts and convert to integers
            a, b = map(int, line.split())
            
            # Calculate and print the GCD
            print(gcd(a, b))
            
        except (ValueError, IndexError):
            # If a line is malformed (e.g., not two numbers),
            # skip it and continue to the next one.
            # Jutge.org inputs are usually well-formed, but this is safer.
            continue
