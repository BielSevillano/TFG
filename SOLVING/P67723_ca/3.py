
import sys

def main():
    for line in sys.stdin:
        line = line.strip()
        if line:
            try:
                a, b = map(int, line.split())
                
                # Euclidean algorithm
                while b:
                    a, b = b, a % b
                
                print(a)
            except (ValueError, IndexError):
                # In case of malformed lines, just skip them.
                continue

if __name__ == "__main__":
    main()
