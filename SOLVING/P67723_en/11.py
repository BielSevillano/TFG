
def gcd(a, b):
    """
    Computes the greatest common divisor of two numbers using the Euclidean algorithm.
    """
    while b:
        a, b = b, a % b
    return a

# Read two integers from a single line of input
try:
    a, b = map(int, input().split())
    # Calculate and print the greatest common divisor
    print(gcd(a, b))
except (EOFError, ValueError):
    # This handles cases where input is not provided or is malformed.
    # On many platforms, the program can simply end when input stream closes.
    pass
