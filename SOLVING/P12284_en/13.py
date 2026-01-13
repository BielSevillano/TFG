
import sys
from collections import Counter
import heapq

# Read the first line to start the loop.
# sys.stdin.readline() returns an empty string '' at the end of the file.
line = sys.stdin.readline()

# The loop continues as long as we read non-empty lines from the input.
while line:
    # Strip whitespace. If the line becomes empty, it was a blank line.
    line = line.strip()
    if not line:
        # Read the next line and continue to the start of the loop.
        line = sys.stdin.readline()
        continue

    try:
        # Parse n (number of words) and k (number of results) from the line.
        n, k = map(int, line.split())
        
        # Read the next n lines, each containing one word.
        words = [sys.stdin.readline().strip() for _ in range(n)]

        # Use collections.Counter to efficiently count word frequencies.
        # This creates a dictionary-like object: {'word': count}.
        counts = Counter(words)

        # Use heapq.nsmallest to find the k most frequent words.
        # This is generally more efficient than a full sort, with a
        # complexity of O(U log k) where U is the number of unique words.
        # The key for comparison is a tuple: (-frequency, word).
        # - The negative frequency ensures sorting in descending order of counts.
        # - The word itself serves as the tie-breaker, sorted alphabetically.
        top_k = heapq.nsmallest(k, counts.items(), key=lambda item: (-item[1], item[0]))

        # Print the word from each of the (word, count) tuples in the result.
        # The result from nsmallest is a list sorted according to the key.
        for word, _ in top_k:
            print(word)
        
        # Print the separator as required by the problem statement.
        print('----------')

    except (ValueError, IndexError):
        # This handles cases where a line is malformed (e.g., n and k are not
        # valid integers) or if input ends unexpectedly. We break the loop.
        break

    # Read the line that should contain n and k for the next test case.
    line = sys.stdin.readline()
