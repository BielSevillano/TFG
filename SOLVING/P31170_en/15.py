
import sys

def main():
    try:
        line = sys.stdin.readline()
        if line:
            n = int(line)
            for i in range(1, 11):
                result = n * i
                print(f"{n} * {i} = {result}")
    except (ValueError, IndexError):
        # In case of empty or invalid input, do nothing.
        pass

if __name__ == "__main__":
    main()
