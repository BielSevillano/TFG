
import sys

def main():
  """
  Reads a natural number from standard input and prints its number of digits.
  """
  # Read the entire input as a string and remove leading/trailing whitespace.
  # For a single number input, sys.stdin.read() is simple and effective.
  # .strip() handles newlines and any other surrounding whitespace.
  n_str = sys.stdin.read().strip()

  # The number of digits is simply the length of the string representation.
  # This correctly handles the edge case of 0 ('0' has length 1) and
  # is efficient as it avoids any type conversion to integer.
  if n_str:
    print(len(n_str))

if __name__ == "__main__":
  main()
