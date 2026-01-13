
import sys

def main():
    try:
        line = sys.stdin.readline()
        if not line:
            return
        n = int(line)
        for i in range(1, 11):
            print(f"{n} * {i} = {n * i}")
    except (ValueError, IndexError):
        # Handles empty input or non-integer input gracefully
        # Although problem statement guarantees valid input, this is good practice
        pass

if __name__ == "__main__":
    main()
