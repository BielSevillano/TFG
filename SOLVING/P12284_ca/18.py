
import sys
from collections import Counter

try:
    # Read all input at once and split by any whitespace.
    # This is efficient and robust to different input formatting.
    tokens = sys.stdin.read().split()
except:
    # Handle empty input.
    tokens = []

# Use an index to traverse the flat list of tokens.
idx = 0
while idx < len(tokens):
    try:
        # Read n and k for the current test case.
        n = int(tokens[idx])
        k = int(tokens[idx + 1])
        idx += 2
        
        # Get the n words for this case using a list slice.
        words = tokens[idx : idx + n]
        idx += n
        
        # Use collections.Counter for efficient frequency counting.
        word_counts = Counter(words)
        
        # Sort the (word, count) pairs.
        # The key is a tuple: (-count, word).
        # This sorts primarily by count in descending order (due to the negation)
        # and secondarily by word in ascending lexicographical order as a tie-breaker.
        sorted_items = sorted(
            word_counts.items(), 
            key=lambda item: (-item[1], item[0])
        )
        
        # Print the top k words.
        # The problem guarantees that 1 <= k <= number of distinct words,
        # so this loop is safe.
        for i in range(k):
            print(sorted_items[i][0])
        
        # Print the separator line.
        print("----------")

    except (ValueError, IndexError):
        # This exception handles cases of malformed input or the end of the
        # token list, gracefully terminating the program.
        break
