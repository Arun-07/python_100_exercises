# Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
# Suppose the following input is supplied to the program: Hello world!
# Then, the output should be:
'''
UPPER CASE 1
LOWER CASE 9
'''

string = input("Enter a string: ")
upper_case, lower_case = 0, 0
for letter in string:
    if 96 < ord(letter) < 123: # we can also use .islower() method here
        lower_case += 1
    elif 64 < ord(letter) < 91: # and .isupper() method here
        upper_case += 1

print('UPPER CASE %d\nLOWER CASE %d' % (upper_case, lower_case))
