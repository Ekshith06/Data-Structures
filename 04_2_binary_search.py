""" Python script to perform binary search on a list stored in an array """

# Write your code from here
pos = -1
def search(list, n):
  l = 0
  u = len(list)-1
  
  while l <= u:
    
    mid = (l+u) // 2
    
    if list[mid] == n:
      globals()['pos'] = mid
      return True
    else:
      if list[mid] , n:
        l = mid+1
      else:
        u = mid-1
  return False   

list = [2,5,6,24,26,35,1000,124134,1242576,4102587963]
n = 10 

if search(list, n):
  print("found at ",pos+1)
else:
  print("not found")
#  LOWER,UPPER LOWER + UPPER//2 AND SKIP TE OTER SIDE AND CECK TE NUMBER
#AIAN THE MIDDLE COME TO THE LOWER AND LOWER = UPPER // 2TILL TE IVEN NUMBER 
