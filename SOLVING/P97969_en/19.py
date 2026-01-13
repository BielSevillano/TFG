
import sys

def count_a_s():
    """
    Reads a sequence of characters from standard input until a period '.'
    is encountered, and prints the number of 'a's in that sequence.
    """
    count = 0
    while True:
        char = sys.stdin.read(1)
        # Stop if end of input or period is found
        if not char or char == '.':
            break
        # Increment count if the character is 'a'
        if char == 'a':
            count += 1
    print(count)

if __name__ == '__main__':
    count_a_s()
