
import sys
from collections import Counter

# This program solves the "Most frequent words" problem by processing
# multiple test cases from standard input.

# To handle various input formatting (like space or newline separators) robustly
# and efficiently, we read the entire standard input at once, split it into
# a list of tokens (words and numbers), and create an iterator over them.
try:
    tokens = iter(sys.stdin.read().split())
except IOError:
    tokens = iter([])

# We loop indefinitely, processing one test case per iteration.
# The loop terminates when there are no more tokens to form a valid test case.
while True:
    try:
        # Each test case starts with two integers: n (number of words) and k.
        n = int(next(tokens))
        k = int(next(tokens))
    except (StopIteration, ValueError):
        # If StopIteration or ValueError occurs, it means the end of input
        # has been reached, or the input is malformed. In either case,
        # we stop processing.
        break

    # We read the next n tokens from the iterator, which correspond to the words
    # for the current test case. A list comprehension is a concise way to do this.
    words = [next(tokens) for _ in range(n)]

    # collections.Counter is a highly optimized dictionary subclass for counting
    # hashable objects. It efficiently computes the frequency of each word.
    counts = Counter(words)

    # To find the k most frequent words, we sort the items of the counter.
    # The `sorted` function's `key` parameter allows for custom sorting logic.
    # We use a lambda function that returns a tuple, which enables multi-level sorting.
    # Python compares tuples element by element.
    # 1. Primary sort key: Frequency in descending order. We use `-item[1]`
    #    because Python's sort is ascending, and sorting by the negative of a
    #    number achieves descending order. `item[1]` is the count (frequency).
    # 2. Secondary sort key (for ties in frequency): The word itself, in
    #    lexicographical (alphabetical) ascending order. `item[0]` is the word.
    sorted_items = sorted(counts.items(), key=lambda item: (-item[1], item[0]))

    # After sorting, the first k elements of the list are the ones we need.
    # We iterate through this slice of the list and print each word.
    for i in range(k):
        # Each `item` in `sorted_items` is a (word, count) tuple. We print the word,
        # which is the first element (index 0).
        print(sorted_items[i][0])

    # As required by the problem statement, we print a separator line of
    # 10 dashes after the output for each test case.
    print("----------")
