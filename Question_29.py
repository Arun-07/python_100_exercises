# Define a function that can accept two strings as input and concatenate them and then print it in console.

def concat_func(s1, s2):
    return s1 + ' ' + s2

str_1, str_2 = input().split(',')
print(concat_func(str_1, str_2))
