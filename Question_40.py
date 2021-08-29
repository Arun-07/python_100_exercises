# Write a program which accepts a string as input to print "Yes" 
# if the string is "yes" or "YES" or "Yes", otherwise print "No".

user_input = input('Enter yes or no: ')
print('Yes') if user_input.casefold() == 'yes' else print('No')    
