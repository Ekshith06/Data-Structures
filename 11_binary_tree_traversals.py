""" Python Script to create a binary tree and perform various traversals """
###EKSHITH.KOLLA
##122010322044
"""
binary tree == every node can have 0,1,2 child nodes
full binary tree == which every node other than leaf nodes has 0 or 2 children
it shouls contain 0 or 2 cildren then it is called full binary tree.
complete binary tree two conditions:
--->all the levels except the last level completely filled with nodes
--->last level     --> completely filled
                   --->left to right
perfect binaray tree:
all inteernal nodes - 2children
leaf node same level
Depth First Traversals: 
(a) Inorder (Left, Root, Right) : 4 2 5 1 3 
(b) Preorder (Root, Left, Right) : 1 2 4 5 3 
(c) Postorder (Left, Right, Root) : 4 5 2 3 1
Breadth First or Level Order Traversal : 1 2 3 4 5
-"""

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
 
 
# A function to do inorder tree traversal
def printInorder(root):
 
    if root:
 
        # First recur on left child
        printInorder(root.left)
 
        # then print the data of node
        print(root.val),
 
        # now recur on right child
        printInorder(root.right)
 
 
# A function to do postorder tree traversal
def printPostorder(root):
 
    if root:
 
        # First recur on left child
        printPostorder(root.left)
 
        # the recur on right child
        printPostorder(root.right)
 
        # now print the data of node
        print(root.val),
 
 
# A function to do preorder tree traversal
def printPreorder(root):
 
    if root:
 
        # First print the data of node
        print(root.val),
 
        # Then recur on left child
        printPreorder(root.left)
 
        # Finally recur on right child
        printPreorder(root.right)
 
 
# Driver code
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print "Preorder traversal of binary tree is"
printPreorder(root)
 
print "\nInorder traversal of binary tree is"
printInorder(root)
 
print "\nPostorder traversal of binary tree is"
printPostorder(root)




"""
#output
Preorder traversal of binary tree is
1 2 4 5 3 
Inorder traversal of binary tree is
4 2 5 1 3 
Postorder traversal of binary tree is
4 5 2 3 1"""

##print(my_bst)
##print(my_heap)
##
##
##       _345 _
##      /     \
##  ___12     777
## /         /  \
##14        10   13
##  \
##   2
####
####
####        ______74_______
####       /              \
####    __34__           ___11___
####   /     \         /        \
#### 451      145     459       0413
#### / \     / \     / \       /   \
####0   2   4   6   8   10    12    14
####
####
####         _______14______
####        /               \
####    ___13__            __12__
####   /       \          /      \
####  11        9        7        10
#### /  \      / \      / \      /  \
####4    2    3   8    6   0    5    1
