""" Python Script to create a binary search tree and perform search operation 
EKSHITH.KOLLA
12010322044"""
def binaraysearch (arr, l, r, x):
    if r >= 1:
        mid = 1 + (r-1) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binaraysearch(arr, l, mid-1, x)
        else:
            return binaraysearch(arr, mid+1, r, x)
    else:
        return -1
arr = [23, 32, 345, 67, 44, 55, 121]
x = 121

result = binaraysearch(arr, 0, len(arr)-1, x)
 if result != -1:
     print("element found ")
 else:
     print("elment not found ")
  

"""METHOD2"""
#Written by EKSHITH.KOLLA
#Date:31/7/2021
#This Program does the Binary Search of a Given Number of Elements in an Array
import numpy as np
num=int(input("Enter The 4-digit Number without zero except in one's place: "))
arr= []
low,high=0,num
for i in range(0,(num+1),1):
    y=arr.append(str(input("Enter Element "+str(i)+": ")))
    y=arr.sort()
key=str(input("Enter the Element to be searched: "))
if(key>str(arr[num])):
    print("Element not found")
else: 
    mid=round((low+high)/2)
    while(low<=high):
        if(key==arr[mid]):
            res=mid
            break
        elif(arr[mid]>key):
            mid=mid-1
        else:
            mid=mid+1
print(arr)
print("Element "+str(key)+" is found at ",mid)


