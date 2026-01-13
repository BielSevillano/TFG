
import sys

text = sys.stdin.read()
sequence = text.split('.', 1)[0]
count = sequence.count('a')
print(count)
