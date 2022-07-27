""" Python script for
   - Representing sparse matrix
   - Sparse matrix addition
   - Sparse matrix transpose  """

# Write your code from here
"""sprase matrix: majority of elements aare zeroes
   it take less memory storage"""
#Represting sprse matrix:
"""row: index of row where non zero element is locted
coloumn: index of coloumn where non zero element is locted
value: value of non ero else locted at index(row,coloumn)"""

"""
sparse martrix addition: 
adding of two matrix 
add_01 = mat_01+mat_02
"""

ekshth.kolla
122010322044

import numpy as np
from scipy.sparse import csr_matrix

row_1_44 = np.array([0, 0, 1, 1, 2])
col_1_44 = np.array([0, 1, 2, 0, 2])
val_1_44 = np.array([5, 54, 25, 12, 45])
"""
row    col   val(data)
0      0       5
0      1      54     
1      2      25
1      0      12
2      2      45
"""

sparse_matrix_01 = csr_matrix((val_1_44, (row_1_44, col_1_44)),shape = (3, 3)).toarray()

print("First Sparse Matrix : ", sparse_matrix_01)# prinnting first matrix


row_2_44 = np.array([0, 0, 1, 1, 2])
col_2_44 = np.array([2, 1, 1, 0, 2])
val_2_44 = np.array([9, 7, 5, 48, 94])
sparse_matrix_02 = csr_matrix((val_2_44, (row_2_44, col_2_44)),shape = (3, 3)).toarray()
"""
row    col   val
0      2       9
0      1       7     
1      1       5
1      0      48
2      2      94
"""

print("Second Sparse Matrix : ", sparse_matrix_02)#priting second matrix
#addition:
add_matrix = sparse_matrix_01 + sparse_matrix_02
print("Addtion of the two matrices is : ", add_matrix)
#subtraction:
subtract_matrix = sparse_matrix_01 - sparse_matrix_02
print("Subtraction of the two matrices is : ", subtract_matrix)
#transpose:
print("Transpose of the given matrix is ", sparse_matrix_01.transpose())

   
