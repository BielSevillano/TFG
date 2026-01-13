
import sys

def main():
    """
    Reads a sequence of characters from standard input until a period '.' is found,
    and then prints the number of occurrences of the letter 'a' in that sequence.
    """
    count = 0
    while True:
        char = sys.stdin.read(1)
        # Stop if we reach the end of the input or the delimiter '.'
        if not char or char == '.':
            break
        if char == 'a':
            count += 1
    print(count)

if __name__ == "__main__":
    main()
