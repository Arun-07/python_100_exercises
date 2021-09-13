# Define a custom exception class which takes a string message as attribute.

class CustomException(Exception):
    '''Exception raised for custom purpose.
    Atttibutes:
        message -- explanation of error
    '''
    def __init__(self, msg):
        self.msg = msg

num = int(input())

try:
    if num < 10:
        raise CustomException("Input is less than 10")
    elif num > 10:
        raise CustomException("Input is grater than 10")
except CustomException as ce:
    print("The error raised: " + ce.msg)

