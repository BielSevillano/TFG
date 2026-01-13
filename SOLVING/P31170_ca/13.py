
import sys

def main():
    try:
        line = sys.stdin.readline()
        if not line:
            return
        
        n = int(line)
        
        for i in range(1, 11):
            result = n * i
            print(f"{n} x {i} = {result}")

    except (ValueError, IndexError):
        # In case of empty input or non-integer input, we just exit gracefully.
        # The problem statement guarantees a valid natural number, but this is for robustness.
        pass

if __name__ == "__main__":
    main()
