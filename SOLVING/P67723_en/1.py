
import sys

def main():
    try:
        line = sys.stdin.readline()
        if not line:
            return
        
        a, b = map(int, line.split())
        
        while b:
            a, b = b, a % b
            
        print(a)

    except (ValueError, IndexError):
        # Handles potential malformed input, though problem spec implies correct input.
        pass

if __name__ == "__main__":
    main()
