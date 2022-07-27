""" Python Script to perform all 5 arthmetic operations +, -, /, *, exponential """

# Write your code from here
def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
#divison are of two types floar and float
def division(x,y): #float
    return x // y
# as per operatin te symbols are returned 
  
print ("select operation")

print("a.add")

print('b.subtract')

print('c.multiply')

print("d.division")

choice = input("Enter choice(a/b/c/d): ")

    # Check if choice is one of the four options
if choice in ('a', 'b', 'c', 'd'):
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == 'a':
        print(f'{num1} + {num2} = {add(num1, num2)}')

    elif choice == 'b':
        print(f'{num1} - {num2} = {subtract(num1, num2)}')
          
    elif choice == 'c':
        print(f'{num1} * {num2} = {multiply(num1, num2)}')


    elif choice == 'd':
        print(f'{num1} // {num2} = {division(num1, num2)}')

else:
    print("Invalid Input")
