
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
    try:
      a, b = map(int, line.split())
      result = gcd(a, b)
      print(result)
    except (ValueError, IndexError):
      # Handles empty or malformed lines, though the problem implies valid input.
      continue

if __name__ == "__main__":
  main()
