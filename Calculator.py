import math

# Define operations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def square_root(x):
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
                print(num1, "+", num2, "=", add(num1, num2))

            elif choice == '2':
                print(num1, "-", num2, "=", subtract(num1, num2))

            elif choice == '3':
                print(num1, "*", num2, "=", multiply(num1, num2))

            elif choice == '4':
                if num2 == 0:
                    print("Error: Division by zero is not allowed!")
                else:
                    print(num1, "/", num2, "=", divide(num1, num2))

        elif choice == '5':
            num = float(input("Enter a number to find its square root: "))
            if num < 0:
                print("Error: Square root of a negative number is not real!")
            else:
                print(f"Square root of {num} is {square_root(num):.2f}")

        else:
            print("Invalid choice! Please select a valid operation.")

if __name__ == "__main__":
    Calculator()
