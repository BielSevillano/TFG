
import sys

def main():
    for line in sys.stdin:
        n_str = line.strip()
        if n_str:
            print(len(n_str))

if __name__ == "__main__":
    main()
