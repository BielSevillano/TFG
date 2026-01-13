
import sys

def main():
    try:
        line = sys.stdin.readline()
        if not line:
            return
        n = int(line)
        for i in range(1, 11):
            result = n * i
            print(f"{n} * {i} = {result}")
    except (IOError, ValueError):
        # In case of empty input or non-integer input, just exit.
        return

if __name__ == "__main__":
    main()
