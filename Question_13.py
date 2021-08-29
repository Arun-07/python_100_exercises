# Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose the following input is supplied to the program: hello world! 123
# Then, the output should be: 
'''
LETTERS 10
DIGITS 3
'''

string = input()
letters, digits = 0, 0
for letter in string:
    if letter.isalpha():
        letters += 1
    elif letter.isdigit():
        digits += 1

print(f'LETTERS {letters}\nDIGITS {digits}')
