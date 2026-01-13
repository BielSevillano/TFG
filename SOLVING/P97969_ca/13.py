
import sys

def main():
    """
    Reads a sequence of characters until a period is found,
    counts the number of 'a's, and prints the count.
    """
    count = 0
    # Process input character by character for memory efficiency
    # in case of very large inputs beyond the period.
    # iter(callable, sentinel) is an efficient way to do this.
    for char in iter(lambda: sys.stdin.read(1), ''):
        if char == '.':
            break
        if char == 'a':
            count += 1
    
    print(count)

if __name__ == "__main__":
    main()
