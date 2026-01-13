
import sys

def gcd(a, b):
  """
  Calculates the greatest common divisor of two numbers using the Euclidean algorithm.
  """
  while b:
    a, b = b, a % b
  return a

try:
  # Read the two numbers from a single line of input.
  # The input is expected to consist of two space-separated integers.
  line = sys.stdin.readline()
  if line:
    a, b = map(int, line.split())
    # Calculate and print the greatest common divisor.
    print(gcd(a, b))
except (ValueError, IndexError):
  # This block handles potential errors if the input is not as expected,
  # although for this specific problem on Jutge.org, the input format
  # is guaranteed to be correct.
  pass
