# Define a class named American and its subclass NewYorker.

class American:
    def printNationality(self):
        return 'American'

class NewYorker(American):
    def printState(self):
        return 'NewYorker'


person = NewYorker()
print(person.printNationality())
print(person.printState())
