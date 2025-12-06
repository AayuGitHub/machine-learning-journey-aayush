# functions.py

def make_smoothie(ingredient1, ingredient2):
    return ingredient1 + " + " + ingredient2

def function_name():
    # Code block
    print("Hello, Dhruvi!")

# function_name()

def greet():
    print("Hello, Dhruvi! Welcome to Python.")

# greet()

def greet(name):
    print(f"Hello, {name}! Welcome to Python.")

# greet("Aayush")

def add_numbers(num1, num2):
    result = num1 + num2
    return result

sum_result = add_numbers(5, 10)
# print(sum_result)

def multiply(x, y):
    return x * y

multiply_result = multiply(10, 10)
print(multiply_result)

def greet(name="Dhruvi"):
    print(f"Hello, {name}! Welcome to Python.")

greet()
greet("Aayush")

def greet(name="Dhruvi"):
    """
    This function greets the person passed in as the 'name'.
    If no name is provided, it greets 'Dhruvi'.
    """
    print(f"Hello, {name}! Welcome to Python.")

print(greet.__doc__)