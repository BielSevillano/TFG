
import sys

def main():
    try:
        n_str = sys.stdin.readline()
        if not n_str:
            return
        
        n = int(n_str)
        
        for i in range(1, 11):
            result = n * i
            sys.stdout.write(f"{n} x {i} = {result}\n")
            
    except (IOError, ValueError):
        # In case of empty input or non-integer input, just exit gracefully.
        # The problem statement guarantees a valid input, but this is good practice.
        return

if __name__ == "__main__":
    main()
