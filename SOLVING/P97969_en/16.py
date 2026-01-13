
import sys

def main():
    """
    Reads a sequence of characters from standard input until a period is encountered,
    then counts and prints the number of occurrences of the letter 'a'.
    """
    count = 0
    # The problem can be solved efficiently by reading the entire input,
    # splitting it by the first period, and then counting 'a's in the first part.
    # This is generally faster than reading character by character due to fewer
    # system calls.
    try:
        # Read all input until EOF
        full_input = sys.stdin.read()
        # The sequence is everything before the first period
        sequence = full_input.split('.', 1)[0]
        # Use the highly optimized string.count() method
        count = sequence.count('a')
        print(count)
    except Exception:
        # Handle potential errors, though unlikely given the problem constraints.
        # This part ensures the program doesn't crash on unexpected input.
        print(0)

if __name__ == "__main__":
    main()
