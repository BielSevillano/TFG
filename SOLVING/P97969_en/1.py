
import sys

def main():
    """
    Reads a sequence of characters from standard input until a period '.' is found,
    and counts the occurrences of the letter 'a'.
    """
    count = 0
    for line in sys.stdin:
        period_pos = line.find('.')
        if period_pos != -1:
            # Period found in this line. Count 'a's before it and stop.
            count += line[:period_pos].count('a')
            break
        else:
            # No period in this line, count 'a's in the whole line.
            count += line.count('a')
    
    print(count)

if __name__ == "__main__":
    main()
