
import sys
from collections import Counter

def solve():
    """
    Reads multiple test cases from stdin, and for each case,
    finds the k most frequent words.
    """
    try:
        # Read all whitespace-separated tokens from the input at once.
        # This is efficient for typical competitive programming input sizes
        # and robustly handles different spacings and newlines.
        tokens = sys.stdin.read().split()
    except (IOError, IndexError):
        # Handle cases with no input or read errors.
        tokens = []

    # If there are no tokens, there's nothing to process.
    if not tokens:
        return

    # Create an iterator to consume tokens one by one.
    it = iter(tokens)

    # Process test cases until the token iterator is exhausted.
    while True:
        try:
            # Read n (number of words) and k (number of results to show).
            n = int(next(it))
            k = int(next(it))

            # Read the n words for the current test case.
            words = [next(it) for _ in range(n)]

            # Use collections.Counter for an efficient word frequency count.
            counts = Counter(words)

            # Sort the unique words based on the specified criteria:
            # 1. Primary sort key: Frequency in descending order.
            #    This is achieved by using the negative of the count.
            # 2. Secondary sort key (for ties): Lexicographical (alphabetical)
            #    order in ascending order.
            sorted_words = sorted(counts.keys(), key=lambda word: (-counts[word], word))
            
            # Print the top k words from the sorted list.
            for i in range(k):
                print(sorted_words[i])

            # Print the separator line as required after each test case.
            print("----------")

        except StopIteration:
            # This exception naturally occurs when the iterator 'it' is exhausted,
            # signaling the end of all test cases.
            break
        except (ValueError, IndexError):
            # Gracefully handle malformed input (e.g., non-integer values for n/k)
            # or incomplete test cases.
            break

# Execute the main solution function.
solve()
