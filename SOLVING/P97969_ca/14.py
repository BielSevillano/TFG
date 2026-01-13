
import sys

def solve():
    text = sys.stdin.read()
    
    end_index = text.find('.')
    
    if end_index == -1:
        sequence = text
    else:
        sequence = text[:end_index]
        
    count = sequence.count('a')
    
    print(count)

solve()
