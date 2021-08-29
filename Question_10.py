# Write a program that accepts a sequence of whitespace separated words 
# as input and prints the words after removing all duplicate words and sorting them alphanumerically.
# Suppose the following input is supplied to the program:
# hello world and practice makes perfect and hello world again
# Then, the output should be: again and hello makes perfect practice world

seq_of_words  = input().split(' ')

unique_words = list(set(word for word in seq_of_words))

print(' '.join(sorted(unique_words)))
