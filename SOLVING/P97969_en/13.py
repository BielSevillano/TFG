
import sys

def main():
    """
    Reads a sequence of characters from standard input until a period '.'
    is encountered or the input stream ends. It counts the number of
    occurrences of the character 'a' and prints the total count.
    """
    count = 0
    while True:
        char = sys.stdin.read(1)
        # Stop if we reach the end of the input (EOF) or find a period.
        if not char or char == '.':
            break
        # If the character is 'a', increment the counter.
        if char == 'a':
            count += 1
    
    print(count)

if __name__ == "__main__":
    main()
