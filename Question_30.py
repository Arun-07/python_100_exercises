# Define a function that can accept two strings as input and print 
# the string with maximum length in console. If two strings have 
# the same length, then the function should print all strings line by line.

def longest_string(s1, s2):
    if len(s1) == len(s2):
        print(s1 + '\n' + s2)
    else:
        print(s1) if len(s1) > len(s2) else print(s2)

str_1, str_2 = input().split(',')
longest_string(str_1, str_2)
