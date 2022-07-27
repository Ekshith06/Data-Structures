""" Python Script to implement various sorting techniques: 
    - Insertion sort
    - Selection Sort
    - Bubble Sort
    - Merge Sort
    - Quick Sort 
    [Compare with Python's Built-In Sorting Functions also]  """

# Write your code from here
#Sorting is any process of arranging items systematically,


#bubble sort
list = []
num = int(input("enter how many numbers you want to enter"))
print("enter values")
for e in range (num):
    list.append(int(input()))
print("unsorted list:",list)
for j in range(len(list)-1):
    for i in range(len(list) - 1):
        if list[i] > list[i+1]:
            list[i], list[i+1] = list[i+1], list[i] #swap+
            print(list)
print("sorted list",list)



#SELECTION SORT
class SelectionSort:
    def __init__(self,a):
        self.arr = a

    def selsort(self):
        for i in range(len(self.arr)):
            min_idx = i
            for j in range(i+1,len(self.arr)):
                if self.arr[min_idx]>self.arr[j]:
                    min_idx=j
            self.arr[i],self.arr[min_idx]=self.arr[min_idx],self.arr[i]
            print("Output After Pass ",i)
            print(self.arr)
    
    def printlist(self):
        print("Elements after Sort: ",end=" ")
        for i in self.arr:
            print(i,end=" ")
        print()

# Driver Code
n =int(input("Enter the number of elements: "))
l=[]
for i in range(n):
    l.append(int(input("Enter the Elements: ")))
print("Elements Before Sort: ",l)
Sobj=SelectionSort(l)
Sobj.selsort()
Sobj.printlist()




#INSERTION SORT
class InsertionSort:
    def __init__(self,a):
        self.arr = a

    def insertsort(self):
        for i in range(len(self.arr)):
            for j in range(i,0,-1):
                if self.arr[j-1]>self.arr[j]:
                    self.arr[j-1],self.arr[j]=self.arr[j],self.arr[j-1]
            print("Output After Pass ",i)
            print(self.arr)

    def printlist(self):
        print("Elements after Sort: ",end=" ")
        for i in self.arr:
            print(i,end=" ")
        print()

# Driver Code
n =int(input("Enter the number of elements: "))
l=[]
for i in range(n):
    l.append(int(input("Enter the Elements: ")))
print("Elements Before Sort: ",l)
Iobj=InsertionSort(l)
Iobj.insertsort()
Iobj.printlist()



#MERGE SORT:

def mergeSort(arr):
    if len(arr) > 1:      # Finding the mid of the array
        mid = len(arr)//2 # Dividing the array elements
        L = arr[:mid]     # into 2 halves
        R = arr[mid:]     # Sorting the first half
        mergeSort(L)      # Sorting the second half
        mergeSort(R)
        i = j = k = 0     # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
 # Checking whether any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
def printList(arr):     #to print the list
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()
  
# Driver Code
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is", end="\n")
    printList(arr)
    mergeSort(arr)
    print("Sorted array is: ", end="\n")
    printList(arr)

    
    
#QUICK SORT
def partition(arr,low,high):
   i = ( low-1 )
   pivot = arr[high] # pivot element
   for j in range(low , high):
      # If current element is smaller
      if arr[j] <= pivot:
         # increment
         i = i+1
         arr[i],arr[j] = arr[j],arr[i]
   arr[i+1],arr[high] = arr[high],arr[i+1]
   return ( i+1 )

def quickSort(arr,low,high):
   if low < high:
      # index
      pi = partition(arr,low,high)
      # sort the partitions
      quickSort(arr, low, pi-1)
      quickSort(arr, pi+1, high)
# main
arr = [2,5,3,8,6,5,4,7]
n = len(arr)
quickSort(arr,0,n-1)
print ("Sorted array is:")
for i in range(n):
   print (arr[i],end=" ")

##refrence from suraj sir
# Python program for implementation of Insertion Sort

def insertion_sort(list_of_numbers):
    for i in range(1, len(list_of_numbers)):
        print("Iteration - ", i , "Input list = ", list_of_numbers)
        current_element = list_of_numbers[i]
        predecessor_index = i -1
        while (predecessor_index >=0) and (current_element < list_of_numbers[predecessor_index]):
            list_of_numbers[predecessor_index+1]=list_of_numbers[predecessor_index]
            predecessor_index -= 1
        list_of_numbers[predecessor_index+1] = current_element




# Python program for implementation of Selection Sort


def selection_sort(list_of_numbers):
    for i in range(len(list_of_numbers)):
        print("Iteration - ", i+1 , "Input list = ", list_of_numbers)
        minimum_value_index = i
        for j in range(i+1, len(list_of_numbers)):
            if list_of_numbers[minimum_value_index] > list_of_numbers[j]:
                minimum_value_index = j
        list_of_numbers[i], list_of_numbers[minimum_value_index] = list_of_numbers[minimum_value_index], list_of_numbers[i]



# Python program for implementation of Bubble Sort

def bubble_sort(list_of_numbers):
    for i in range(len(list_of_numbers)-1):
        print("Iteration - ", i+1 , "Input list = ", list_of_numbers)
        for j in range(0, len(list_of_numbers)-i-1):
            if list_of_numbers[j] > list_of_numbers[j+1] :
                list_of_numbers[j], list_of_numbers[j+1] = list_of_numbers[j+1], list_of_numbers[j]
            


# Python program for implementation of Quicksort Sort
def partition(list_of_numbers, low, high):
    i = low	 # index of smaller element
    pivot = list_of_numbers[high]	 # pivot
    for j in range(low, high):
        if list_of_numbers[j] <= pivot:
            list_of_numbers[i], list_of_numbers[j] = list_of_numbers[j], list_of_numbers[i]
            i = i+1
    list_of_numbers[i], list_of_numbers[high] = list_of_numbers[high], list_of_numbers[i]
    return i


def quick_sort(list_of_numbers, low, high):
    global counter
    print("Iteration - ", counter , "Input list = ",list_of_numbers)
    counter = counter + 1
    if low < high:
        partition_index = partition(list_of_numbers, low, high)
        quick_sort(list_of_numbers, low, partition_index - 1)
        quick_sort(list_of_numbers, partition_index + 1, high)
        #print(list_of_numbers)


# Python program for implementation of MergeSort
def merge_sort(list_of_numbers):
    global counter
    print("Iteration - ", counter , "Input list = ",list_of_numbers)
    counter = counter + 1
    if len(list_of_numbers) > 1:
        middle_index = len(list_of_numbers)//2
        left_sublist = list_of_numbers[:middle_index]
        right_sublist = list_of_numbers[middle_index:]
        merge_sort(left_sublist)
        merge_sort(right_sublist)

        i = j = k = 0
        while i < len(left_sublist) and j < len(right_sublist):
            if left_sublist[i] < right_sublist[j]:
                list_of_numbers[k] = left_sublist[i]
                i += 1
            else:
                list_of_numbers[k] = right_sublist[j]
                j += 1
            k += 1
        while i < len(left_sublist):
            list_of_numbers[k] = left_sublist[i]
            i += 1
            k += 1
        while j < len(right_sublist):
            list_of_numbers[k] = right_sublist[j]
            j += 1
            k += 1


# Python program for implementation of heap Sort

# To heapify subtree rooted at index i.
# n is size of heap


def heapify(arr, n, i):
    global counter
    print("Iteration - ", counter , "Input list = ",arr)
    counter = counter + 1
    largest = i # Initialize largest as root
    l = 2 * i + 1	 # left = 2*i + 1
    r = 2 * i + 2	 # right = 2*i + 2

    # See if left child of root exists and is
    # greater than root
    if l < n and arr[largest] < arr[l]:
        largest = l

    # See if right child of root exists and is
    # greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r
        # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i] # swap
        # Heapify the root.
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    # Build a maxheap.
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)
    # One by one extract elements
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i] # swap
        heapify(arr, i, 0)


list_of_numbers = [19, 1, 11, 13, 5, 6, 9]
counter=1            

##insertion_sort(list_of_numbers)
##selection_sort(list_of_numbers)
##bubble_sort(list_of_numbers)
##quick_sort(list_of_numbers, 0, len(list_of_numbers)-1)
##merge_sort(list_of_numbers)
heap_sort(list_of_numbers)


print ("Elements after sorting: ", list_of_numbers)


##Output of Insertion Sort
##
##Iteration -  1 Input list =  [19, 1, 11, 13, 5, 6, 9]
##Iteration -  2 Input list =  [1, 19, 11, 13, 5, 6, 9]
##Iteration -  3 Input list =  [1, 11, 19, 13, 5, 6, 9]
##Iteration -  4 Input list =  [1, 11, 13, 19, 5, 6, 9]
##Iteration -  5 Input list =  [1, 5, 11, 13, 19, 6, 9]
##Iteration -  6 Input list =  [1, 5, 6, 11, 13, 19, 9]
##Elements after sorting:  [1, 5, 6, 9, 11, 13, 19]

##Output of Selection Sort
##Iteration -  0 Input list =  [19, 1, 11, 13, 5, 6, 9]
##Iteration -  1 Input list =  [1, 19, 11, 13, 5, 6, 9]
##Iteration -  2 Input list =  [1, 5, 11, 13, 19, 6, 9]
##Iteration -  3 Input list =  [1, 5, 6, 13, 19, 11, 9]
##Iteration -  4 Input list =  [1, 5, 6, 9, 19, 11, 13]
##Iteration -  5 Input list =  [1, 5, 6, 9, 11, 19, 13]
##Iteration -  6 Input list =  [1, 5, 6, 9, 11, 13, 19]
##Elements after sorting:  [1, 5, 6, 9, 11, 13, 19]

##Output of Bubble Sort
##Iteration -  0 Input list =  [19, 1, 11, 13, 5, 6, 9]
##Iteration -  1 Input list =  [1, 11, 13, 5, 6, 9, 19]
##Iteration -  2 Input list =  [1, 11, 5, 6, 9, 13, 19]
##Iteration -  3 Input list =  [1, 5, 6, 9, 11, 13, 19]
##Iteration -  4 Input list =  [1, 5, 6, 9, 11, 13, 19]
##Iteration -  5 Input list =  [1, 5, 6, 9, 11, 13, 19]
##Elements after sorting:  [1, 5, 6, 9, 11, 13, 19]

##Output of Quick Sort
##[19, 1, 11, 13, 5, 6, 9]
##[1, 5, 6, 9, 19, 11, 13]
##[1, 5, 6, 9, 19, 11, 13]
##[1, 5, 6, 9, 19, 11, 13]
##[1, 5, 6, 9, 19, 11, 13]
##[1, 5, 6, 9, 19, 11, 13]
##[1, 5, 6, 9, 19, 11, 13]
##[1, 5, 6, 9, 11, 13, 19]
##[1, 5, 6, 9, 11, 13, 19]
##Elements after sorting:  [1, 5, 6, 9, 11, 13, 19]
