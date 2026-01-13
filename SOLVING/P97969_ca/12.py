
import sys

count = 0
input_text = sys.stdin.read()

for char in input_text:
    if char == '.':
        break
    elif char == 'a':
        count += 1

print(count)
