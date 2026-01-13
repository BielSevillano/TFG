
import sys

def main():
    """
    Reads a sequence of characters until a period is found,
    and counts the occurrences of the letter 'a'.
    """
    count = 0
    # Use a buffer to read in chunks for efficiency
    buffer = sys.stdin.read(4096)
    while buffer:
        period_index = buffer.find('.')
        if period_index != -1:
            # Period found in the current buffer
            # Process the part of the buffer before the period and stop
            count += buffer[:period_index].count('a')
            break
        else:
            # No period in this buffer, process the whole buffer and read more
            count += buffer.count('a')
            buffer = sys.stdin.read(4096)
    
    print(count)

if __name__ == "__main__":
    main()
