
import sys
from collections import Counter

def solve():
    """
    Reads all input tokens, processes test cases, and prints results.
    """
    try:
        # Read the entire input and split into tokens. This is efficient for
        # typical competitive programming constraints and handles various
        # whitespace patterns (spaces, newlines) seamlessly.
        tokens = sys.stdin.read().split()
    except (IOError, OSError):
        # Handle potential errors during input reading
        tokens = []

    # Use an index to iterate through the tokens
    idx = 0
    while idx < len(tokens):
        try:
            # Parse n and k for the current test case
            n = int(tokens[idx])
            k = int(tokens[idx + 1])
            idx += 2

            # Slice the next n tokens as the words for this case
            words = tokens[idx:idx + n]
            idx += n
            
            # Use collections.Counter to efficiently count word frequencies
            word_counts = Counter(words)

            # Sort the (word, count) pairs.
            # The sorting key is a tuple: (-count, word).
            # Python sorts tuples element by element.
            # - By -count: Sorts by frequency in descending order.
            # - By word: For ties in frequency, sorts by word in ascending
            #   (lexicographical) order.
            sorted_items = sorted(word_counts.items(), key=lambda item: (-item[1], item[0]))

            # Print the top k words
            for i in range(k):
                # The problem guarantees that k is valid, so no index error here.
                print(sorted_items[i][0])
            
            # Print the separator line after each test case
            print("----------")

        except (ValueError, IndexError):
            # This robustly handles malformed n/k values or an incomplete
            # final test case by simply ending the processing loop.
            break

solve()
