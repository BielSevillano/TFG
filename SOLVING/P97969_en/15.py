
import sys

count = 0
for line in sys.stdin:
    if '.' in line:
        # The period is in this line, so it's the last part of the sequence.
        # We take the substring before the first period.
        segment = line.split('.', 1)[0]
        count += segment.count('a')
        # Stop reading further input.
        break
    else:
        # This line is part of the sequence, but not the last one.
        # Count all 'a's in the whole line.
        count += line.count('a')

print(count)
