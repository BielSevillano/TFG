
import sys

def main():
    """
    Reads characters from stdin until a period is found,
    and counts the occurrences of the letter 'a'.
    """
    count = 0
    # Read the entire input stream at once for efficiency.
    # The problem statement guarantees a period exists.
    full_input = sys.stdin.read()
    
    # Iterate through the characters of the input string.
    for char in full_input:
        # Stop processing when the end-of-sequence marker is found.
        if char == '.':
            break
        # Increment the counter if the character is 'a'.
        if char == 'a':
            count += 1
            
    # Print the final count.
    print(count)

if __name__ == "__main__":
    main()
