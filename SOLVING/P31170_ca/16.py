
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
    except (ValueError, IndexError):
        # Handles potential empty lines or invalid input gracefully, though problem statement guarantees valid input.
        pass

if __name__ == "__main__":
    main()
