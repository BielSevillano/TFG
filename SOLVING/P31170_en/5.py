
import sys

def main():
    try:
        line = sys.stdin.readline()
        if not line:
            return
        n = int(line)
        for i in range(1, 11):
            print(f"{n} x {i} = {n * i}")
    except (IOError, ValueError):
        # In case of empty input or non-integer input, just exit gracefully.
        # This handles edge cases for platforms that might test with weird inputs.
        pass

if __name__ == "__main__":
    main()
