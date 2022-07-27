""" Python Script to check whether a given number is perfect  """

# Write your code from here
lower = int(input("enter the lower limit"))
upper = int(input("enter the upper limit"))
#finding the perfect numbers in the given limit
for num in range(lower,upper+1):
#here the upper +1 is used bcz of in the given range the lastnum should be considerd
  result = 0
  for pn in range(1,num):
    if (num%pn)==0:
      result=result+pn
  if num==result:
    print(f"{num} is a perfect number in the given limits")
'''for example if 3 is taken to find the perfect number then 3 51,352,but not in the same itself'''
