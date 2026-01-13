
import sys
from collections import Counter

try:
    # Create an iterator over all whitespace-separated tokens from standard input.
    # This approach is robust to different ways of formatting the input (e.g.,
    # words on the same line or on different lines) and is generally efficient.
    tokens = iter(sys.stdin.read().split())

    # Process test cases in a loop until the input stream is exhausted.
    while True:
        # Read n, the number of words, and k, the number of most frequent words to output.
        # This will raise StopIteration if there are no more tokens, which is caught below.
        n = int(next(tokens))
        k = int(next(tokens))

        # Read the next n tokens as the words for the current case.
        words = [next(tokens) for _ in range(n)]

        # Use collections.Counter to count the occurrences of each word efficiently.
        word_counts = Counter(words)

        # Sort the word-count pairs. The sorting criteria are:
        # 1. Frequency in descending order. Achieved by sorting on the negative of the count.
        # 2. Word in alphabetical (lexicographical) order as a tie-breaker.
        sorted_items = sorted(word_counts.items(), key=lambda item: (-item[1], item[0]))

        # Print the top k words. The problem guarantees that k is valid
        # (1 <= k <= number of unique words), so we don't need to check for
        # index out of bounds.
        for i in range(k):
            print(sorted_items[i][0])

        # As required, print a separator line at the end of each case's output.
        print("----------")

except StopIteration:
    # This exception indicates the end of the input stream. We catch it and
    # do nothing (pass), allowing the program to terminate cleanly.
    pass
