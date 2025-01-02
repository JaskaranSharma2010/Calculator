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

def square(x):
    return x*x

def square_root(x):
    if x < 0:
        return "Error: Square root of a negative number is not real!"
    return math.sqrt(x)

def calculate_percentage(part, whole):
    return (part / whole) * 100

# Main calculator function
def Calculator():
    while True:
        print("\nSelect An Operation: \n 1. Add \n 2. Subtract \n 3. Multiply \n 4. Divide \n 5. Find Square Root \n 6. Find The Sqaure  \n 7.Find The Percentage \n 8. Exit")
        
        choice = input("Enter Your Choice: ")

        if choice == '7':
            part = float(input("Enter the part: "))
            whole = float(input("Enter the whole number: "))
            result = calculate_percentage(part, whole)
            print(f"The percentage is: {result:.2f}%")
            continue

        if choice == '8':
            print("Thanks for Using The Program!!")
            break

        if choice in ['1', '2', '3', '4','5']:
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

        if choice == '6':
            Sqaure_Num = int(input("Enter The No. To Find The Square: "))
            print("The Sqaure Of", Sqaure_Num, "is :-  ", Sqaure_Num * Sqaure_Num)
                


            

        else:
            print("Invalid choice! Please select a valid operation.")

if __name__ == "__main__":
    Calculator()    
