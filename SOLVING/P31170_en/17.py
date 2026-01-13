
import sys

def main():
    """
    Reads a number n from standard input and prints its multiplication table.
    """
    try:
        # Jutge.org problems often expect reading until EOF,
        # but this problem description implies a single number.
        # However, to be robust for typical online judge systems,
        # we can process all lines from the input.
        for line in sys.stdin:
            line = line.strip()
            if line:
                n = int(line)
                for i in range(1, 11):
                    result = n * i
                    print(f"{n} * {i} = {result}")
    except (ValueError, IndexError):
        # In case of malformed input, the program will simply exit.
        # This is generally acceptable in competitive programming
        # where input is assumed to follow the specified format.
        pass

if __name__ == "__main__":
    main()
