""" Python Script to create a Circular singly linked list for adding and 
deleting a Node. """
#ekshith.kolla
#122010322044
"""
Circular linked list is a linked list where all nodes are connected to form a circle.
there is no NULL at the end
A circular linked list can be a singly circular linked list or doubly circular linked list.
Data represents the data stored in the node, and next is the pointer that will point to the next node. 
Head will point to the first element of the list, and tail will point to the last element in the list.
"""
class node:
    def __init__(self,value,add):
        self.value=value
        self.nxtadd=add
"""To implement a circular singly linked list, we take an external pointer that points to the last node of the list. 
If we have a pointer last pointing to the last node, then last -> next will point to the first node. 
"""
def insert(root,v):
    traverser = root
    newnode=node(v,root)
    if root.nxtadd == None :
        root.nxtadd =newnode
    else:
        while traverser.nxtadd != root:
            traverser = traverser.nxtadd
        traverser.nxtadd =newnode
    traverser.nxtadd=newnode 


def display(root):
    traverser = root
    while traverser.nxtadd != root :
        print(traverser.value)
        traverser=traverser.nxtadd
    print(traverser.value)
    
    
def delete(root):
    traverser = root
    while traverser.nxtadd != root:
        if traverser.nxtadd.nxtadd == root:
            traverser.nxtadd = traverser.nxtadd.nxtadd
            break
        if ((traverser.value) %2)!= 0 :
            traverser.value = traverser.nxtadd.value
            traverser.nxtadd = traverser.nxtadd.nxtadd
        else:
            traverser=traverser.nxtadd
    # traverser.nxtadd=None



def main():
    root=node(101,None)
    insert(root,899)
    insert(root,455)
    insert(root,624)
    insert(root,753)
    delete(root)
    display(root)

    
if __name__ == '__main__':
    main()
    
