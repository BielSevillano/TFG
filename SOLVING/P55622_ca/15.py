
import sys

def main():
    try:
        # Read the input as a string from standard input
        line = sys.stdin.readline().strip()
        
        # If the line is not empty, it contains the number
        if line:
            # The number of digits is simply the length of the string representation
            print(len(line))
            
    except (IOError, ValueError):
        # This part handles potential errors, though not expected with problem constraints
        # It's good practice for robust programs.
        pass

if __name__ == "__main__":
    main()
