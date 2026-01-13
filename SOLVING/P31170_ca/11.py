
import sys

def main():
  try:
    n = int(sys.stdin.readline())
    for i in range(1, 11):
      result = n * i
      print(f"{n} x {i} = {result}")
  except (IOError, ValueError):
    # This part is generally not needed for competitive programming
    # platforms like Jutge.org, as input is guaranteed to be correct.
    # However, it's good practice for robust code.
    pass

if __name__ == "__main__":
  main()
