
import sys
from collections import Counter

try:
    # Create an iterator over all whitespace-separated tokens in the standard input.
    # This efficiently handles various input layouts (words on one line or multiple).
    tokens = iter(sys.stdin.read().split())

    # Process test cases in a loop until the input is fully consumed.
    while True:
        # Read n (the number of words) and k (the number of frequent words to find).
        # The `next()` function will raise a StopIteration exception when the tokens
        # iterator is exhausted, which is caught below to terminate the program.
        n = int(next(tokens))
        k = int(next(tokens))

        # Read the n words for the current test case using a list comprehension.
        words = [next(tokens) for _ in range(n)]

        # Use collections.Counter to get the frequency of each word in O(n) time.
        word_counts = Counter(words)

        # Sort the (word, count) pairs from the counter.
        # The sorting key is a tuple, which Python sorts element-wise.
        # 1. -item[1]: Sorts by frequency in descending order (by negating the count).
        # 2. item[0]: For ties in frequency, sorts by word in ascending lexicographical order.
        sorted_items = sorted(word_counts.items(), key=lambda item: (-item[1], item[0]))

        # Print the first k words from the sorted list, each on a new line.
        for i in range(k):
            print(sorted_items[i][0])

        # Print the required separator at the end of the case's output.
        print("----------")

except StopIteration:
    # This exception is the expected signal for the end of input.
    # The 'pass' statement allows the program to exit gracefully.
    pass
