
import sys

def main():
    """
    Reads a natural number from standard input and prints its number of digits.
    """
    try:
        # Read the entire standard input and remove leading/trailing whitespace.
        # For a single number, this will capture it regardless of newlines.
        line = sys.stdin.read().strip()
        
        # Check if the input is not empty before proceeding.
        if line:
            # The number of digits of a non-negative integer is simply the
            # length of its string representation.
            # The problem guarantees a "natural number", which is non-negative.
            print(len(line))
            
    except Exception:
        # In case of any unexpected error, the program will exit gracefully.
        # This is for robustness, as Jutge.org provides valid inputs.
        pass

if __name__ == "__main__":
    main()
