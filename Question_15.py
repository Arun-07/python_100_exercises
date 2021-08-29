# Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
# Suppose the following input is supplied to the program: 9
# Then, the output should be: 11106

v = input()
# print(int(v) + int(v*2) + int(v*3) + int(v*4))    This is specific to this problem

# Below code can be made dynamic
res = 0
for i in range(1, 5):
    res += int(v*i)
print(res)

