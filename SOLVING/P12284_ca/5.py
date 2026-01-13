
import sys
from collections import Counter

try:
    # Create a generator that yields words from the standard input one by one.
    # This approach is memory-efficient as it processes the input as a stream
    # and handles various whitespace arrangements (e.g., words on same/different lines).
    input_stream = (word for line in sys.stdin for word in line.split())
    
    # Process test cases until the input stream is exhausted.
    while True:
        # Read the number of words (n) and the number of results to show (k).
        # The next() function will raise a StopIteration exception if the input stream
        # is empty, which is caught by the outer try-except block to end the program.
        n = int(next(input_stream))
        k = int(next(input_stream))
        
        # Collect the n words for the current test case from the stream.
        words = [next(input_stream) for _ in range(n)]
        
        # Use collections.Counter to efficiently count the frequency of each word.
        counts = Counter(words)
        
        # Sort the unique words based on the specified criteria:
        # 1. Primary key: Frequency, in descending order.
        # 2. Secondary key: The word itself, in lexicographical (alphabetical)
        #    ascending order, used as a tie-breaker.
        # This is achieved by using a tuple `(-frequency, word)` as the sort key.
        # The negative sign on the frequency effectively reverses the sort order for that part.
        sorted_items = sorted(
            counts.items(), 
            key=lambda item: (-item[1], item[0])
        )
        
        # Print the top k words from the sorted list.
        # The problem statement guarantees that k is at most the number of unique words.
        for i in range(k):
            # sorted_items[i] is a tuple ('word', count), we print only the word.
            print(sorted_items[i][0])
        
        # Print the required separator line after each test case.
        print("----------")
        
except StopIteration:
    # This exception is the standard signal that an iterator (our input_stream)
    # is exhausted. We catch it and simply pass, allowing the program to
    # terminate gracefully after processing all available input.
    pass
