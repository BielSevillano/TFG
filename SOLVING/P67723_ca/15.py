
import sys

try:
    line = sys.stdin.readline()
    if line:
        a, b = map(int, line.split())
        
        while b:
            a, b = b, a % b
            
        print(a)
except (ValueError, IndexError):
    pass
