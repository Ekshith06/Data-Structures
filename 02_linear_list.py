""" Python Script to read a linear list of items and store it in an array.
   - Copy the contents from one array to another array
   - Copy the contents from one array to another array in reverse order
   - Delete the duplicate elements from an array. """

# Write your code from here
# Written by Ekshith.Kolla
# Date: 26/5/2021
import array as arr

value_list = [1, 2, 3, 4, 5]

# Python Script to read a linear list of items and store it in an array.
x = arr.array('i', value_list)
print(x)

# Copy the contents from one array to another array.

y = [None] * len(x)
for i in range(0, len(x)):
    y[i] = x[i]
print(y)

# Copy the contents from one array to another array in reverse order.

z = [None] * len(x)
for i in range(0, len(x)):
    z[i] = x[len(x) - i - 1]
    
print(z)

# Delete the duplicate elements from an array.

res = []

for i in x :
    if i not in res :
        res.append(i)
print(res)

"""
=============== RESTART: C:/Users/lenovo/Downloads/linear_list.py ==============
array('i', [1, 2, 3, 4, 5])
[1, 2, 3, 4, 5]
[5, 4, 3, 2, 1]
[1, 2, 3, 4, 5]

"""
