
import sys

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def main():
    try:
        line = sys.stdin.readline()
        if not line:
            return
        a, b = map(int, line.split())
        result = gcd(a, b)
        print(result)
    except (ValueError, IndexError):
        # Handles cases with non-integer input or empty lines,
        # although problem statement implies clean input.
        pass

if __name__ == "__main__":
    main()
