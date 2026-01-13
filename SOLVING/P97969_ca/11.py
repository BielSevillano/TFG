
import sys

text = sys.stdin.read()
sequence = text.split('.', 1)[0]
a_count = sequence.count('a')
print(a_count)
