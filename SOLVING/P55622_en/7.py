
import sys

for line in sys.stdin:
    line = line.strip()
    if line:
        n_str = str(int(line))
        print(len(n_str))
