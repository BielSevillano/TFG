
import sys

# The problem states that the input is a single natural number.
# We can read this number as a string from the standard input.
# The readline() method reads one line, including the trailing newline character.
line = sys.stdin.readline()

# The strip() method removes leading/trailing whitespace, including the newline.
# The result is the string representation of the number.
number_as_string = line.strip()

# The number of digits of a number is simply the length of its string representation.
# The len() function gives us this length.
print(len(number_as_string))
