
import sys

def main():
    try:
        line = sys.stdin.readline()
        if not line:
            return
        
        n_str = line.strip()
        
        # The int() function handles potential leading zeros or whitespace.
        # For example, int("007") becomes 7.
        n = int(n_str)
        
        # Converting the integer back to a string gives its canonical representation.
        # str(7) is "7", str(0) is "0", str(123) is "123".
        # The length of this string is the number of digits.
        print(len(str(n)))

    except (IOError, ValueError):
        # Handle potential empty input or non-integer input gracefully,
        # though the problem statement implies valid input.
        return

if __name__ == "__main__":
    main()
