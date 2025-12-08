# error_handling.py

try:
    # Code that might raise an error
    x = 1 / 0  # Division by zero error
except ZeroDivisionError:
    # Handle the error here
    print("Oops! You can't divide by zero!")
finally:
    print("This will run no matter what!")

try:
    # Try to open a file
    with open("non_existent_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("Oops! The file was not found.")
finally:
    print("This will run no matter what!")

try:
    # Try to open a file
    x = 10 / int(input("Enter a number: "))
except ZeroDivisionError:
    print("Oops! You can't divide by zero!")
except ValueError:
    print("Oops! You entered an invalid number")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

x = 10
y = 0

print(f"x = {x}, y = {y}")

try:
    result = x / y
except ZeroDivisionError:
    print("Oops! You can't divide by zero!")    