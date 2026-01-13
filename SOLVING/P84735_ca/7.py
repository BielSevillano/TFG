
import sys

for line in sys.stdin:
    try:
        a, b = map(int, line.split())

        if b == 0:
            # Although the problem states b >= 1, handle this edge case.
            continue
        
        rem = a % b
        
        if rem == 0:
            result = a
        else:
            result = a + (b - rem)
            
        print(result)

    except (ValueError, IndexError):
        # This handles empty lines or malformed input, effectively
        # stopping the program when input ends.
        break
