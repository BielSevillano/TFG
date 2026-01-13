
import sys

count = 0
# Read the entire input into a string and iterate over its characters.
for char in sys.stdin.read():
    # If the character is a period, it marks the end of the sequence.
    if char == '.':
        break
    # If the character is the one we are looking for, increment the counter.
    if char == 'a':
        count += 1

# Print the final count.
print(count)
