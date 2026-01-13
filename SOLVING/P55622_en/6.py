
import sys

def main():
    """
    Reads a natural number from standard input and prints its number of digits.
    """
    # sys.stdin.readline() reads a single line from the input, including the
    # trailing newline character.
    # .strip() removes any leading/trailing whitespace, including the newline.
    # The input is guaranteed to be a natural number, so the resulting
    # string will contain only digits.
    number_str = sys.stdin.readline().strip()
    
    # The number of digits is simply the length of the string representation.
    # This works for any non-negative integer, including 0.
    if number_str:
        print(len(number_str))

if __name__ == "__main__":
    main()
