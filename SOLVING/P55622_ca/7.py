
import sys

def main():
    try:
        # Read the number from standard input as a string
        # input() reads a line and strips the trailing newline
        n_str = sys.stdin.readline().strip()

        # The number of digits is simply the length of its string representation.
        # This works correctly for all non-negative integers, including 0.
        if n_str:
            print(len(n_str))

    except (IOError, ValueError):
        # Handle potential errors, though unlikely with the problem constraints
        # (e.g., empty input or non-numeric input if the problem was different)
        # For this specific problem, the input is guaranteed to be a natural number.
        pass

if __name__ == "__main__":
    main()
