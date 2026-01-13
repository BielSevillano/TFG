
import sys
from collections import Counter

def solve():
    """
    Reads tokens from stdin as a stream, processes each test case,
    and prints the k most frequent words according to the specified criteria.
    """
    # Create an iterator that yields tokens (words and numbers) from standard input.
    # This approach is memory-efficient as it processes the input as a stream.
    tokens = (token for line in sys.stdin for token in line.split())

    while True:
        try:
            # Read n and k for the next test case from the token stream.
            n_str = next(tokens)
            k_str = next(tokens)
            n = int(n_str)
            k = int(k_str)
        except (StopIteration, ValueError):
            # If the token stream is exhausted or a token is not a valid integer,
            # it means there are no more test cases. We break the loop.
            break

        # Read the n words for the current test case into a list.
        # The problem guarantees that n words will follow n and k.
        words = [next(tokens) for _ in range(n)]

        # 1. Count the frequency of each word using collections.Counter.
        word_counts = Counter(words)

        # 2. Convert the counter's items to a list and sort it.
        #    The sorting criteria are:
        #    - Primary: Frequency in descending order.
        #    - Secondary: Word in ascending (lexicographical) order.
        #    We use a lambda function with a tuple `(-count, word)` as the key.
        #    Negating the count achieves descending order for the primary key.
        #    Python's tuple comparison handles the secondary key automatically.
        sorted_items = sorted(word_counts.items(), key=lambda item: (-item[1], item[0]))

        # 3. Print the first k words from the sorted list.
        for i in range(k):
            print(sorted_items[i][0])
        
        # 4. Print the separator line as required by the problem statement.
        print("----------")

solve()
