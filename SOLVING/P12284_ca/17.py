
import sys
from collections import Counter

try:
    tokens = sys.stdin.read().split()
except IOError:
    tokens = []

idx = 0
num_tokens = len(tokens)

while idx < num_tokens:
    try:
        n = int(tokens[idx])
        k = int(tokens[idx + 1])
        idx += 2

        if idx + n > num_tokens:
            break
        
        words = tokens[idx:idx + n]
        idx += n

    except (ValueError, IndexError):
        break

    counts = Counter(words)

    # Sort items by frequency (descending) and then by word (ascending)
    # The key is a tuple: (-frequency, word).
    # Negating frequency achieves descending order.
    sorted_items = sorted(counts.items(), key=lambda item: (-item[1], item[0]))

    # Print the top k words
    for i in range(k):
        print(sorted_items[i][0])
    
    print("----------")
