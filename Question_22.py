# Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically.
# Suppose the following input is supplied to the program:
# 'New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.'
# Then, the output should be:
# 2:2 \n 3.:1 \n 3?:1 \n New:1 \n Python:5 \n Read:1 \n and:1 \n between:1 \n choosing:1 \n or:2 \n to:1

string = input("Enter the string: ").split(' ')

my_dict = {}

for item in string:
    my_dict[item] = string.count(item)

for k,v in sorted(my_dict.items(), key=lambda k: k):
    print(k,':',v)

