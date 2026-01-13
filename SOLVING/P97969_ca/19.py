
import sys

input_text = sys.stdin.read()
count = 0

for char in input_text:
    if char == '.':
        break
    if char == 'a':
        count += 1

print(count)
