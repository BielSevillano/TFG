
import sys

def solve():
    """
    Reads numbers from stdin and prints their multiplication tables.
    """
    for line in sys.stdin:
        # Strip whitespace (like the newline character) and convert to an integer
        try:
            n = int(line.strip())
        except (ValueError, IndexError):
            # Skip empty or non-numeric lines
            continue

        # Iterate from 1 to 10 to generate the table
        for i in range(1, 11):
            result = n * i
            # Print in the format "n * i = result"
            print(f"{n} * {i} = {result}")

if __name__ == "__main__":
    solve()
