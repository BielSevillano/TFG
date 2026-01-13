
import sys
from collections import Counter
import heapq

def main():
    """
    Reads words from standard input, finds the k most frequent,
    and prints them according to the problem specification.
    """
    try:
        # Create an iterator over all whitespace-separated tokens in the input.
        # This is a robust way to handle various input formattings.
        tokens = iter(sys.stdin.read().split())
        
        # Process test cases until the input tokens are exhausted.
        while True:
            n = int(next(tokens))
            k = int(next(tokens))
            
            # Use a generator expression within Counter for memory efficiency.
            # It reads n words and counts their frequencies directly.
            counts = Counter(next(tokens) for _ in range(n))
            
            # Use heapq.nsmallest to efficiently find the top k items.
            # The key for selection is a tuple: (-count, word).
            # -item[1] makes the selection order by frequency descending.
            # item[0] makes the tie-breaker order by word ascending (lexicographical).
            # nsmallest returns a list sorted by this key.
            top_k_items = heapq.nsmallest(k, counts.items(), key=lambda item: (-item[1], item[0]))
            
            # Print the words from the resulting top k list.
            for word, count in top_k_items:
                print(word)
            
            # Print the separator as required for each test case.
            print("----------")
            
    except (StopIteration, ValueError):
        # StopIteration is raised by next() on an exhausted iterator (end of file).
        # ValueError can be raised if int() is called on a non-integer token,
        # which can happen with malformed input or trailing whitespace.
        # In either case, we gracefully stop processing.
        pass

if __name__ == "__main__":
    main()
