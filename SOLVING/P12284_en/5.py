
import sys
from collections import Counter

def main():
    """
    Main function to solve the problem. Reads all input, processes test cases,
    and prints the k most frequent words for each case.
    """
    try:
        # Read all whitespace-separated tokens from stdin at once and create an iterator.
        # This is a common and efficient pattern for competitive programming.
        all_tokens = iter(sys.stdin.read().split())
    except IOError:
        return

    while True:
        try:
            # Read n and k for the current test case.
            n = int(next(all_tokens))
            k = int(next(all_tokens))

            # Read the n words for this case into a list.
            words = [next(all_tokens) for _ in range(n)]

            # Use collections.Counter for efficient frequency counting.
            word_counts = Counter(words)

            # Sort the items (word, count) from the counter.
            # The primary sort key is frequency in descending order (-item[1]).
            # The secondary sort key is the word in lexicographical ascending order (item[0]).
            sorted_items = sorted(
                word_counts.items(),
                key=lambda item: (-item[1], item[0])
            )

            # Print the first k words from the sorted list.
            for i in range(k):
                print(sorted_items[i][0])
            
            # Print the separator line as required.
            print("----------")

        except StopIteration:
            # The iterator is exhausted, meaning no more input.
            break

if __name__ == "__main__":
    main()
