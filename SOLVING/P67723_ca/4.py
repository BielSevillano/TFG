
import sys

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def main():
    try:
        # Assuming a single line of input with two numbers
        line = sys.stdin.readline()
        if line:
            a, b = map(int, line.split())
            result = gcd(a, b)
            print(result)
    except (ValueError, IndexError):
        # Handle potential empty lines or malformed input gracefully
        pass

if __name__ == "__main__":
    main()
