
import sys
from collections import Counter

def main():
    """
    Reads multiple test cases from standard input to find the k most frequent words.
    """
    # Create a generator to efficiently iterate over all tokens (words) from stdin.
    # This method is memory-efficient and handles various input formats.
    tokens = (token for line in sys.stdin for token in line.split())

    try:
        # Process test cases in a loop until the input stream is exhausted.
        while True:
            # Read n (number of words) and k (number of top frequent words to show).
            # If the token stream is empty, next() will raise StopIteration,
            # which is caught below to terminate the loop.
            n = int(next(tokens))
            k = int(next(tokens))

            # Read the next n words for the current test case.
            words = [next(tokens) for _ in range(n)]

            # Use collections.Counter to efficiently count the frequency of each word.
            counts = Counter(words)
            
            # Sort the (word, count) pairs. The sorting key is a tuple that ensures
            # sorting by frequency in descending order, and then by word
            # in lexicographical (alphabetical) ascending order for ties.
            sorted_items = sorted(counts.items(), key=lambda item: (-item[1], item[0]))

            # Print the top k words from the sorted list.
            for i in range(k):
                print(sorted_items[i][0])
            
            # Print the required separator after each test case.
            print("----------")

    except StopIteration:
        # This block is executed when the 'tokens' iterator is exhausted,
        # indicating the end of the input. The 'pass' statement allows the
        # program to terminate gracefully.
        pass

if __name__ == "__main__":
    main()
