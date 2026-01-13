
import sys

def main():
    """
    Reads a single line representing a natural number and prints its digit count.
    """
    try:
        # Read a line from standard input.
        # input() reads a line and strips the trailing newline.
        # .strip() is used to remove any potential leading/trailing whitespace.
        line = sys.stdin.readline().strip()
        
        # The problem guarantees the input is a natural number,
        # so we can assume the line is not empty and contains only digits.
        # The number of digits is simply the length of the string.
        if line:
            print(len(line))
            
    except (IOError, ValueError):
        # This part handles potential errors during input, though unlikely
        # given the problem constraints on Jutge.org.
        # For a simple problem like this, error handling is often omitted,
        # but it's good practice.
        pass

if __name__ == "__main__":
    main()
