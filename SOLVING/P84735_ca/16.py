
import sys

case_counter = 1
for line in sys.stdin:
    try:
        a, b = map(int, line.split())
    except (ValueError, IndexError):
        continue

    rem = a % b
    
    if rem == 0:
        result = a
    else:
        result = a + (b - rem)
        
    print(f"Case #{case_counter}: {result}")
    
    case_counter += 1
