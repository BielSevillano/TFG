
import sys

def main():
    """
    Reads a sequence of characters until a period is found
    and counts the occurrences of the letter 'a'.
    """
    count = 0
    while True:
        char = sys.stdin.read(1)
        # Stop if end of input is reached or a period is read.
        if not char or char == '.':
            break
        if char == 'a':
            count += 1
    print(count)

if __name__ == "__main__":
    main()
