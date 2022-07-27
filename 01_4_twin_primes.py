""" Python Script to find twin primes upto a specified limit """

# Write your code from here

def is_prime(n):
   
   for i in range(2, n):
      if n % i == 0:
         return False
   return True

def generate_twins(start, end):
   
   for i in range(start, end):
      j = i + 2
      
      if(is_prime(i) and is_prime(j)):
          print(f'{i} and {j}')
        

generate_twins(2, 1000)
