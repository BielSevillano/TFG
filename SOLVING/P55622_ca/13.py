
import sys

def main():
  """
  Reads a natural number from standard input and prints its number of digits.
  """
  try:
    # Read the entire input, which should be a single number.
    # strip() removes any leading/trailing whitespace, including the newline character.
    n_str = sys.stdin.read().strip()
    
    # The number of digits of a natural number is the length of its string representation.
    # An empty input would result in a length of 0, but the problem guarantees a natural number.
    if n_str:
      print(len(n_str))
      
  except Exception as e:
    # This block is for robustness, though not expected to be hit
    # with valid Jutge.org inputs.
    pass

if __name__ == "__main__":
  main()
