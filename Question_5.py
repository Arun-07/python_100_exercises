# Question 5
# Define a class which has at least two methods:
# i. getString: to get a string from console input
# ii. printString: to print the string in upper case.
# Also please include simple test function to test the class methods.

class LowerToUpper:
    def getString(self):
        self.string = input("Enter a lowercase string: ")

    def printString(self):
        return self.string.upper()

string_1 = LowerToUpper()
string_1.getString()
print(string_1.printString())
