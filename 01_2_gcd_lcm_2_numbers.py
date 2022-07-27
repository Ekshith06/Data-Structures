""" Python Script to find GCD and LCM of 2 numbers """

# Write your code from here

def gcd(e, k):   # Recursive function to return gcd of a and b
  
    # if Everything divides 0
    
    if (e == 0):
        return k
    if (k == 0):
        return e
  
    #if both numbers are given same
    
    if (e == k):
        return e
  
 
    #if one is greater than the other
  
    if (e > k):   # if e is greater
        return gcd(e-k, k)
    return gcd(e, k-e)  #k is greater
  

e = 30
k = 45

if(gcd(e, k)):
    print(f"GCD of {e}and {k} is {gcd(e, k)}")
    
else:
    print("invalid (not found)")

    
    
    
    
    
    
# THE NEXT METHOD
def Compute_lcm(e1,e2):
  if e1>e2:
    higher = e1
  else:
    higher = e2
  value = higher
  if higher%e1==0 and higher%e2==0:
    print("lcm of",e1,"and",e2,"is",higher)
  else:
    hiogher = higher+higher
    
    
e1 = int(input("enter the first number:"))  
e2 = int(input("enter the second number:"))  
  
    
    
    
    
    
    
    
