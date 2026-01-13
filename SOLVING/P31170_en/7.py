
import sys

for line in sys.stdin:
    line = line.strip()
    if line:
        try:
            n = int(line)
            for i in range(1, 11):
                print(f"{n} x {i} = {n * i}")
        except ValueError:
            # According to the statement, the input will be a natural number.
            # This is here for robustness against empty or malformed lines.
            pass
