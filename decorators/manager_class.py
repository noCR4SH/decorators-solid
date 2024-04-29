import sys

# Define a class calles Manager that will manage different actions
class Manager:
    # Initialize an empty dictionary to store action names and their functions
    def __init__(self):
        self.actions = {}

    # A method to assign a function to a specific action name
    def assign(self, name):
        # This method returns a decorator which will be used to decorate a function
        def decorate(cb):
            # Store the call back function in the dictionary with given name
            self.actions[name] = cb
        return decorate
    
    # A method to execute a function associated with a given action name
    def execute(self, name):
        # Check if the action name exists in the dictionary
        if name not in self.actions:
            print("Action not defined!")
        else:
            # If the action is defined, executoe the associated function, passing 'self' (the Manager instance)
            self.actions[name](self)

# Create an instance of Manager
manager = Manager()

# Function to handle adding two numbers
@manager.assign("add")
def add(manager):
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print(f"The sum of {a} and {b} is {a + b}")

# Function to handle subtracting two numbers
@manager.assign("subtract")
def subtract(manager):
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print(f"The difference of {a} and {b} is {a - b}")

# Function exit a program
@manager.assign("exit")
def exit_program(manager):
    print("Existing the program..")
    sys.exit(0)


def main_menu():
    print("\nWelcome to the simple calculator!")
    print("1. Add two numbers")
    print("2. Subtract two numbers")
    print("3. Exit")
    choice = input("Enter your choice (1, 2, 3): ")
    return choice

while True:
    choice = main_menu()
    if choice == "1":
        manager.execute("add")
    elif choice == "2":
        manager.execute("subtract")
    elif choice == "3":
        manager.execute("exit")
    else:
        print("Invalid input!")