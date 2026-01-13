
import sys

def main():
  try:
    line = sys.stdin.readline().strip()
    if line:
      print(len(line))
  except (IOError, ValueError):
    # This part is generally not needed for Jutge.org problems
    # as input is well-formed, but it's good practice for robustness.
    pass

if __name__ == "__main__":
  main()
