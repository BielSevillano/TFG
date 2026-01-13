
import sys
from collections import Counter

def solve():
    """
    This function encapsulates the logic to read all input and process it case by case.
    It's designed to be efficient for typical competitive programming scenarios.
    """
    # Create a generator to yield tokens from standard input one by one.
    # This is memory-efficient as it doesn't load the entire input at once.
    tokens = (token for line in sys.stdin for token in line.split())

    try:
        # Loop indefinitely to handle multiple test cases.
        # The loop will be broken by a StopIteration exception when input ends.
        while True:
            # Read the number of words (n) and the number of frequent words to find (k).
            n = int(next(tokens))
            k = int(next(tokens))

            # Read the next n words from the input stream.
            words = [next(tokens) for _ in range(n)]

            # Use collections.Counter to count the frequency of each word efficiently.
            counts = Counter(words)

            # Sort the words based on the specified criteria.
            # 1. Primary key: Frequency, in descending order. Achieved by using -item[1].
            # 2. Secondary key: Word, in lexicographical (alphabetical) ascending order.
            #    This is the tie-breaker.
            sorted_words = sorted(counts.items(), key=lambda item: (-item[1], item[0]))

            # Print the top k words from the sorted list.
            for i in range(k):
                print(sorted_words[i][0])
            
            # Print the required separator after each test case.
            print("----------")

    except StopIteration:
        # This exception is naturally raised by `next(tokens)` when there is no more
        # input to read, signaling the end of all test cases.
        # We simply pass, allowing the program to terminate gracefully.
        pass

if __name__ == "__main__":
    solve()
