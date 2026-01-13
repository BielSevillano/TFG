
import sys

def main():
    """
    Reads a sequence of characters from standard input until a period '.'
    is found, and counts the number of occurrences of the letter 'a'.
    """
    count = 0
    while True:
        char = sys.stdin.read(1)
        if not char or char == '.':
            break
        if char == 'a':
            count += 1
    print(count)

if __name__ == "__main__":
    main()
