
import sys

case_number = 1
for line in sys.stdin:
    try:
        a, b = map(int, line.split())
        
        # We need the smallest multiple of b, let's call it x, such that x >= a.
        # This is equivalent to ceil(a/b) * b.
        # A common way to compute ceiling division ceil(a/b) with integers for a>=0, b>0
        # is using the formula (a + b - 1) // b.
        
        # If a is a multiple of b, say a = k*b.
        # The formula becomes ((k*b + b - 1) // b) * b = k*b = a.
        # If a is not a multiple of b, say a = k*b + r with 0 < r < b.
        # The formula becomes (((k*b+r) + b - 1) // b) * b = ((k+1)*b + r-1 // b) * b = (k+1)*b.
        # Both cases yield the correct result.
        
        result = ((a + b - 1) // b) * b
        
        print(f"Case {case_number}: {result}")
        case_number += 1
    except ValueError:
        # This handles empty lines or lines that do not contain two valid integers.
        pass
