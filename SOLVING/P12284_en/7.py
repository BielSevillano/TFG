
import sys
from collections import Counter

try:
    tokens = sys.stdin.read().split()
except IOError:
    tokens = []

if not tokens:
    sys.exit(0)

it = iter(tokens)

while True:
    try:
        n = int(next(it))
        k = int(next(it))

        words = [next(it) for _ in range(n)]

        counts = Counter(words)
        
        # Sort by frequency (descending) and then by word (alphabetical ascending)
        # The key (-item[1], item[0]) achieves this:
        # -item[1] for descending frequency
        # item[0] for ascending word order in case of a tie in frequency
        sorted_items = sorted(counts.items(), key=lambda item: (-item[1], item[0]))

        for i in range(k):
            print(sorted_items[i][0])
        
        print("----------")

    except StopIteration:
        # This exception signals that the iterator is exhausted,
        # meaning all input has been processed.
        break

