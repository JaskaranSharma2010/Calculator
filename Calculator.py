import math

# Define operations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero is not allowed!"
    return x / y

def square_root(x):
    if x < 0:
        return "Error: Square root of a negative number is not real!"
    return math.sqrt(x)

# Main calculator function
def Calculator():
    while True:
        print("\nSelect An Operation: \n 1. Add \n 2. Subtract \n 3. Multiply \n 4. Divide \n 5. Find Square Root \n 6. Exit")
        
        choice = input("Enter Your Choice: ")

        if choice == '6':
            print("Thanks for Using The Program!!")
            break

        if choice in ['1', '2', '3', '4']:
            num1 = float(input("Enter First Number: "))
            num2 = float(input("Enter Second Number: "))

            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")

            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")

            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")

            elif choice == '4':
                result = divide(num1, num2)
                print(f"{num1} / {num2} = {result}")

        elif choice == '5':
            num = float(input("Enter a number to find its square root: "))
            result = square_root(num)
            print(f"Square root of {num} = {result}")

        else:
            print("Invalid choice! Please select a valid operation.")

if __name__ == "__main__":
    Calculator()
