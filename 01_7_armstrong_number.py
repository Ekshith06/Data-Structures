""" Python Script to find whether a number is armstrong or not """

# Write your code from here

num = int(input("Enter a number: "))

x = str(num)#to find the length  
l=len(x)

sum = 0

# find the sum of the power of each digit of the given number
mun = num
while mun > 0:
   digit = mun % 10
   sum += digit ** l 
   mun //= 10

if num == sum:
   print(f'{num} is an Armstrong number')
else:
   print(f'{num} is not an Armstrong number')
#153,1634 are armstrong numbers
