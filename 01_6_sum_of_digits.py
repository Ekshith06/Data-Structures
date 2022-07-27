""" Python Script to find sum of digits of a number """

# Write your code from here
def get_Sum(e): 
     
    sum = 0
    while (e != 0): 
        
        sum = sum + (e % 10)
        e = e//10
        
    return sum
    
e = 987456
print(get_Sum(e))
