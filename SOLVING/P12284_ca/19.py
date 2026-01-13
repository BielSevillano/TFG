
import sys
from collections import Counter

# This function reads all whitespace-separated tokens from the standard input
# and creates an iterator over them. This approach is efficient and robustly
# handles various input formatting (e.g., words on one line or multiple lines).
try:
    tokens = iter(sys.stdin.read().split())
except IOError:
    tokens = iter([])

# The main loop processes test cases until the input stream is exhausted.
while True:
    try:
        # For each case, first read n (number of words) and k (number to output).
        n = int(next(tokens))
        k = int(next(tokens))

        # Read the next n tokens as words.
        words = [next(tokens) for _ in range(n)]

        # Use collections.Counter to efficiently count the frequency of each word.
        # This results in a dictionary-like object mapping words to their counts.
        counts = Counter(words)

        # Sort the items (word, count pairs) from the counter.
        # The sorting key is a tuple, which allows for multi-level sorting:
        # 1. Primary key: -item[1] (negative count) to sort by frequency descending.
        # 2. Secondary key: item[0] (the word) to sort lexicographically ascending
        #    in case of a tie in frequency.
        sorted_items = sorted(counts.items(), key=lambda item: (-item[1], item[0]))

        # Print the first k words from the sorted list.
        for i in range(k):
            print(sorted_items[i][0])
        
        # As required, print a separator line after each test case's output.
        print("----------")

    except StopIteration:
        # This exception is raised when the 'tokens' iterator has no more items,
        # indicating the end of the input. We break the loop to terminate.
        break
    except (ValueError, IndexError):
        # This handles cases of malformed input and also terminates the program.
        break
