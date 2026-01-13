
import sys

def main():
    try:
        line = sys.stdin.readline()
        if line:
            n = int(line)
            for i in range(1, 11):
                print(f"{n} x {i} = {n * i}")
    except (ValueError, IndexError):
        # Handles potential empty input or non-integer input, though problem statement guarantees valid input.
        pass

if __name__ == "__main__":
    main()
