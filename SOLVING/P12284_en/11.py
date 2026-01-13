
import sys
from collections import Counter

def main():
    """
    Reads words from standard input, finds the k most frequent words for multiple
    test cases, and prints them according to the specified sorting criteria.
    """
    # Create a generator to yield words one by one from standard input.
    # This handles any combination of spaces and newlines between words.
    words_iterator = (word for line in sys.stdin for word in line.split())

    while True:
        try:
            # For each case, first read n and k.
            n = int(next(words_iterator))
            k = int(next(words_iterator))
        except (StopIteration, ValueError):
            # If we can't read n and k, we've reached the end of the input.
            break

        # Read the n words for the current test case.
        case_words = [next(words_iterator) for _ in range(n)]
        
        # Use collections.Counter for an efficient word frequency count.
        word_counts = Counter(case_words)
        
        # Sort the words based on frequency (descending) and then
        # lexicographically (ascending) in case of a tie.
        # The key for sorting is a tuple: (-count, word).
        # Python's tuple comparison sorts by the first element, then the second for ties.
        # The negative sign on the count effectively sorts it in descending order.
        sorted_items = sorted(
            word_counts.items(), 
            key=lambda item: (-item[1], item[0])
        )
        
        # Print the first k words from the sorted list.
        for i in range(k):
            print(sorted_items[i][0])
        
        # Print the separator line after each test case.
        print("----------")

if __name__ == "__main__":
    main()
