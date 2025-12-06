import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

def power(a, b):
    return math.pow(a, b)

def sqrt(a):
    if a < 0:
        return "Error! Square root of negative number."
    return math.sqrt(a)

def log(a):
    if a <= 0:
        return "Error! Logarithm of non-positive number."
    return math.log(a)

def sin(a):
    return math.sin(math.radians(a))

def cos(a):
    return math.cos(math.radians(a))

def tan(a):
    return math.tan(math.radians(a))

def main():
    while True:
        print("\nScientific Calculator")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Power (x^y)")
        print("6. Square Root (√x)")
        print("7. Logarithm (ln x)")
        print("8. Sine (sin x)")
        print("9. Cosine (cos x)")
        print("10. Tangent (tan x)")
        print("11. Exit")

        choice = input("Enter your choice (1-11): ")

        if choice in ('1', '2', '3', '4', '5'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            if choice == "1":
                print(f"Result: {add(num1, num2)}")
            elif choice == "2":
                print(f"Result: {subtract(num1, num2)}")
            elif choice == "3":
                print(f"Result: {multiply(num1, num2)}")
            elif choice == "4":
                print(f"Result: {divide(num1, num2)}")
            elif choice == "5":
                print(f"Result: {power(num1, num2)}")

        elif choice in ('6', '7', '8', '9', '10'):
            num1 = float(input("Enter number: "))
            
            if choice == "6":
                print(f"Result: {sqrt(num1)}")
            elif choice == "7":
                print(f"Result: {log(num1)}")
            elif choice == "8":
                print(f"Result: {sin(num1)}")
            elif choice == "9":
                print(f"Result: {cos(num1)}")
            elif choice == "10":
                print(f"Result: {tan(num1)}")

        elif choice == "11":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1-11.")

if __name__ == "__main__":
    main()
