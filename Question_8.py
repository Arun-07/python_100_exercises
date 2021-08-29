# Question 8
# Write a program that accepts a comma separated sequence of words as input 
# and prints the words in a comma-separated sequence after sorting them alphabetically.
# Suppose the following input is supplied to the program: without, hello, bag, world
# Then, the output should be: bag, hello, without, world

bag_of_words = input().split(',')
print(', '.join(sorted(bag_of_words)))

# one-liner for the same is
# print('The sorted list of words is: ', ', '.join(sorted(input('Enter words separated by coma: ').split(','))))

