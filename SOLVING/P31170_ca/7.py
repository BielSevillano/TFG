
import sys

def main():
  try:
    line = sys.stdin.readline()
    if line:
      n = int(line)
      for i in range(1, 11):
        result = n * i
        print(f"{n} x {i} = {result}")
  except (ValueError, IndexError):
    pass

if __name__ == "__main__":
  main()
