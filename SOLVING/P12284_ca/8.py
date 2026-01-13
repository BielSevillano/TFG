
import sys

line = sys.stdin.readline()

while line:
    try:
        n, k = map(int, line.split())
    except (ValueError, IndexError):
        line = sys.stdin.readline()
        continue

    word_counts = {}
    for _ in range(n):
        word = sys.stdin.readline().strip()
        if word:
            word_counts[word] = word_counts.get(word, 0) + 1
    
    # Sort the items (word, count) from the dictionary.
    # The key is a tuple: (-frequency, word).
    # This sorts primarily by frequency in descending order,
    # and secondarily by word in lexicographical (ascending) order.
    sorted_items = sorted(word_counts.items(), key=lambda item: (-item[1], item[0]))
    
    # The problem guarantees that k is at most the number of distinct words,
    # so we can safely access the first k elements.
    for i in range(k):
        print(sorted_items[i][0])
    
    print("----------")
    
    # Read the first line of the next test case
    line = sys.stdin.readline()
