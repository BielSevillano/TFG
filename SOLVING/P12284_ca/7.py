
import sys
from collections import Counter

def main():
    """
    Reads multiple test cases from standard input to find the k most frequent words.
    For each case, it reads n and k, followed by n words.
    It then prints the k most frequent words, sorted by frequency (descending)
    and then by lexicographical order (ascending) as a tie-breaker.
    A separator line is printed after each case.
    The program terminates upon reaching the end of the input file.
    """
    # Read the first line of a potential test case
    line = sys.stdin.readline()

    # Continue processing as long as there is input
    while line:
        try:
            # Attempt to parse n and k from the line
            n, k = map(int, line.split())
        except (ValueError, IndexError):
            # This handles blank lines that might exist between test cases.
            # If a line cannot be parsed into two integers, we assume it's
            # a separator and try to read the next line to find a new case.
            line = sys.stdin.readline()
            continue

        # Read the n words for the current case using a list comprehension for conciseness
        # .strip() removes leading/trailing whitespace, including the trailing newline
        words = [sys.stdin.readline().strip() for _ in range(n)]

        # Use collections.Counter to efficiently count word frequencies
        counts = Counter(words)

        # Sort the words based on the specified criteria. The key for sorting is a tuple:
        # 1. Negative frequency (-item[1]) to sort in descending order of frequency.
        # 2. The word itself (item[0]) to sort alphabetically as a tie-breaker.
        sorted_items = sorted(counts.items(), key=lambda item: (-item[1], item[0]))

        # Print the top k most frequent words, one per line
        for i in range(k):
            print(sorted_items[i][0])
            
        # Print the separator line as required by the problem statement
        print("----------")
        
        # Read the first line of the next potential test case
        line = sys.stdin.readline()

if __name__ == "__main__":
    main()
