
import sys

def main() -> None:
    """
    Reads a natural number from standard input and prints its number of digits.
    """
    # Read a single line from standard input.
    # The problem guarantees the input is a single natural number.
    line = sys.stdin.readline()
    
    # The input line might be empty if the input stream is closed,
    # or it will contain the number followed by a newline.
    # .strip() removes leading/trailing whitespace, including the newline.
    number_str = line.strip()
    
    # As per the problem statement, the input will be a natural number,
    # so number_str will not be empty. The number of digits is simply
    # the length of its string representation.
    if number_str:
        print(len(number_str))

if __name__ == "__main__":
    main()
