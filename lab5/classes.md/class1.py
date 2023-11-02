class StringManipulator:
    def __init__(self):
        self.input_string = ""

    def getString(self):
        self.input_string = input("Enter a string: ")

    def printString(self):
        print(self.input_string.upper())

# Create an instance of the class
string_manipulator = StringManipulator()

# Get a string from console input
string_manipulator.getString()

# Print the string in uppercase
string_manipulator.printString()
