""" Python Script to find primes numbers upto a specified limit """

# Write your code from here
a_44 = int(input("enter the lower limit"))
b_44 = int(input("enter the upper limit"))
#finding the prime numbers in the given limits

for i in range(a_44,b_44+1):
  
  if i>1:
    for j in range(2,i):
      
      if(i%j==0):
        break
  #braek at that number and agian start form the next number
    else:
      print(i)













