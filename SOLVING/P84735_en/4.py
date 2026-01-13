
import sys

case_number = 1
for line in sys.stdin:
    try:
        a, b = map(int, line.split())
        
        # Calculate the smallest multiple of b that is greater than or equal to a.
        # This can be found using the ceiling of a/b, multiplied by b.
        # An efficient way to calculate ceil(a/b) using integer arithmetic is (a + b - 1) // b.
        
        if a % b == 0:
            result = a
        else:
            result = (a // b + 1) * b
            
        print(f"Case {case_number}: {result}")
        case_number += 1
    except (ValueError, IndexError):
        # Handles potential empty lines at the end of input or malformed lines.
        continue
