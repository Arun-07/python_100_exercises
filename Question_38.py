# With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print 
# the first half values in one line and the last half values in one line.

a_tuple = (1,2,3,4,5,6,7,8,9,10)

l = round(len(a_tuple)/2)

for i in a_tuple[:l]:
    print(i, end=' ')
print()
for j in a_tuple[l:]:
    print(j, end=' ')


# a_tuple = (1,2,3,4,5,6,7,8,9,10)
# l = round(len(a_tuple)/2)
# print(a_tuple[:5])
# print(a_tuple[5:])
