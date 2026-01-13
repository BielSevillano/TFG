
import sys

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def main():
    for line in sys.stdin:
        try:
            a, b = map(int, line.split())
            print(gcd(a, b))
        except (IOError, ValueError):
            break

if __name__ == "__main__":
    main()
