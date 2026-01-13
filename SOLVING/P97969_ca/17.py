
import sys

s = sys.stdin.read()
dot_index = s.find('.')
if dot_index != -1:
    sequence = s[:dot_index]
    print(sequence.count('a'))
else:
    # This case should not happen based on the problem statement,
    # but as a safeguard, we can count in the whole string.
    print(s.count('a'))

