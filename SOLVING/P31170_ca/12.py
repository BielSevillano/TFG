
import sys

def main():
    try:
        n_str = sys.stdin.readline()
        if not n_str:
            return
        n = int(n_str)
        for i in range(1, 11):
            result = n * i
            print(f"{n} x {i} = {result}")
    except (ValueError, IndexError):
        # Handles empty input or non-integer input gracefully, though problem statement guarantees valid input.
        return

if __name__ == "__main__":
    main()
