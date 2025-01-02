def add(x,y):
     return x+y

def substract(x,y):
     return x-y

def multiply(x,y):
     return x*y

def divide(x,y):
     return x/y

def Calculator ():
     while True:
          print("Select An Operation: \n 1. Add \n 2. Substract \n 3. Multiply \n 4. Divide \n 5. Exit")

          choice = input("Enter Your Choice:  ")

          if choice == '5':
               print("Thanks for Using The Program!!")
               break


          if choice in  ['1', '2', '3', '4']:
               num1 = float(input("Enter First Number:  "))
               num2 = float(input("Enter Second Number:  "))

          if choice == '1':
               print(num1, "+", num2, "=", add(num1, num2))

          elif choice == '2':
               print(num1,"-",num2,"=",substract(num1,num2))

          elif choice == '3':
               print(num1,"*",num2,"=",multiply(num1,num2))

          elif choice == '4':
               print(num1,"/",num2,"=",divide(num1,num2))

          

if __name__ == "__main__":
     Calculator()