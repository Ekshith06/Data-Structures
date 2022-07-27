""" Python script to perform linear search in an array. """

# Write your code from here
#122010322044
#ekshith.kolla
"""
start from the leftmost element of liost and one by one compare key with each element in the list
if key matches the element,return true
else return false"""
#code:
def search(list1,key):
  for i in range(len(list1)):#we need to check the key elemnt to each element of the list
    if key == list1[i]:# key value is in the given list
      print("key element is found")
      break#if key element is found it will print and come out of the loop so we used break statement
  
  else:
    print("element is not found")    


list1 = [34,23,5,6,7,1,23,8]
key = int(input("enter the key element:"))
search(list1,key)
"""key = 4 in the range of len(list)
4 ==34   no
4 ==23   no
4 ==5    no
4 ==6    no
4 ==7    no
4 ==1    no
4 ==23   no
4 ==8    no
so we did not found the key in the given list"""
#if we found the elemnt in the list its just breeak up there

