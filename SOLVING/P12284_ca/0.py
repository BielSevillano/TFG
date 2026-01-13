
import sys
from collections import Counter

def main():
    """
    Main function to read test cases from standard input and process them.
    It reads pairs of integers n and k, followed by n words.
    For each case, it finds the k most frequent words and prints them.
    The sorting criteria are frequency (descending) and then lexicographical order (ascending).
    """
    # Read the first line which should contain n and k for the first test case.
    # The loop continues as long as we can read a non-empty line.
    line = sys.stdin.readline()

    while line:
        try:
            # Parse n and k from the line.
            n, k = map(int, line.split())
        except (ValueError, IndexError):
            # This handles potential empty lines between test cases.
            # If a line is empty or malformed, we read the next one and continue.
            line = sys.stdin.readline()
            continue

        # Use collections.Counter for efficient frequency counting.
        counts = Counter()
        for _ in range(n):
            word = sys.stdin.readline().strip()
            counts[word] += 1

        # Get the (word, count) pairs and sort them based on the problem's criteria.
        # The key is a tuple: `(-count, word)`.
        #   - `-count` sorts by frequency in descending order.
        #   - `word` sorts lexicographically in ascending order for ties.
        sorted_word_counts = sorted(counts.items(), key=lambda item: (-item[1], item[0]))

        # The problem guarantees that k is between 1 and the number of distinct words,
        # so we can safely access the first k elements.
        for i in range(k):
            print(sorted_word_counts[i][0])

        # Print the separator line after each test case.
        print("----------")

        # Read the line for the next test case. If it's the end of the file,
        # readline() will return an empty string, and the while loop will terminate.
        line = sys.stdin.readline()

if __name__ == "__main__":
    main()
