# Define a class, which have a class parameter and have a same instance parameter.

class HelloWorld:
    string = 'World'

    def __init__(self, string=None):
        self.string = string


h = HelloWorld('Hello')
print(h.string, HelloWorld.string)

