
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
        # According to the problem statement, the input will always be a valid number.
        # This is here for robustness, but likely won't be triggered.
        pass

if __name__ == "__main__":
    main()
