
import sys

def main():
  """
  Reads numbers from standard input, one per line, and prints the number of digits for each.
  """
  for line in sys.stdin:
    # Strip whitespace, including the trailing newline character
    n_str = line.strip()
    
    # If the line is not empty after stripping, process it
    if n_str:
      # The number of digits is the length of the string representation
      print(len(n_str))

if __name__ == "__main__":
  main()
