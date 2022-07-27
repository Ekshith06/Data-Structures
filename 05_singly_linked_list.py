"""Python script to create a singly linked list for the following operations
   - Insert a Node at Beginning, at Ending and at a given Position
   - Delete a Node at Beginning, at Ending and at a given Position
   - Search, Count the Number of Nodes and Display """

# Write your code from here\
""" starting of the linked list is head
ending value is null or empty
all the nodes will store the refernce of the nxt node
it only contain one link its forward links no backwardlinks
each node contain "data field" and "link(reference)"
 adding are of three methods we can add at the begin or at end and inbetween the linked list
#add begin 
first create node
change new nopde = next which means head 
head --> new node i.e just updating the new node so that the node refernce becomes head    
#add end
create node 
goto last node
ref last node = new node
#add in between
create node
goto node just before required position and new node
x.ref = new node        (z)
z.ref =y"""


# Written by EKSHITH.KOLLA
# Date: 24/7/2021
# This Program may be a menu driven code for Singly Linked List


def Menu():
    print("1. Show the List ")
    print("2. Putting the Node at the Beginning")
    print("3. Putting the Node at the End")
    print("4. Putting the Node at a Given Position")
    print("5. Removing the Node at the Beginning")
    print("6. Removing the Node at the End")
    print("7. Removing the Node at a Given Position")
    print("8. Largest Node in the List")
    print("9. Mean of the Nodes")
    print("10. Sorting the List")
    print("11. Inverse of the List")
    print("12. Leave")
    choice = int(input("Enter your option: "))
    return choice


class LinkedNode:

    def __init__(self, info):
        self.info = info
        self.next = None


# Making SinglyLinkedList category
class SinglyLinkedList:

    def __init__(self):
        self.head = None

    def place_beginning(self, newinfo):
        latest_node = LinkedNode(newinfo)
        latest_node.next = self.head
        self.head = latest_node

    def place_end(self, newinfo):
        latest_node = LinkedNode(newinfo)
        if self.head is None:
            self.head = latest_node
            return
        end = self.head
        while (end.next is not None):
            end = end.next
        end.next = latest_node

    def place_position(self, dis_node, newinfo):
        before_node = self.head
        tempo = dis_node
        found = 0
        while (before_node):
            if before_node.info == dis_node:
                found += 1
                break
            else:
                tempo = None
            before_node = before_node.next
        if tempo is None:
            if found == 0:
                print("The before_node isn't present in LinkedList")
                return
        latest_node = LinkedNode(newinfo)
        latest_node.next = before_node.next
        before_node.next = latest_node

    def delete_beginning(self):
        if self.head is None:
            print("No Node is present to remove")
            return
        print(self.head, " has been deleted")
        self.head = self.head.next

    def delete_end(self):
        if self.head is None:
            print("No Node is present to remove")
            return
        temporary = self.head
        while (temporary.next.next is not None):
            temporary = temporary.next
        print(temporary.next, " has been deleted")
        temporary.next = None

    def delete_position(self, newinfo):
        before_node = self.head
        found = 0
        while (before_node.next is not None):
            if before_node.info == newinfo:
                found += 1
                print(before_node.info, " has been removed")
                break
            else:
                tempo = None
            before_node = before_node.next
        if tempo is None:
            if found == 0:
                print("No Node is present to remove")
                return
        pos = self.head
        while (pos != None):
            if pos.next == before_node:
                previous = pos
                break
            pos = pos.next
        previous.next = before_node.next

    def Display(self):
        dis = self.head
        while (dis):
            print(dis.info)
            dis = dis.next

    def largest_node(self):
        if self.head is None:
            print("No Nodes present")
            return
        dis = self.head.info
        main = self.head
        while (main):
            if dis < main.info:
                dis = main.info
            main = main.next
        print("The Largest Node in the List is: ", dis)

    def mean(self):
        mean = 0
        cou = 0
        men = self.head
        while (men):
            mean = mean + men.info
            men = men.next
            cou += 1
        mean = mean / cou
        print("The Mean of the Nodes is: ", mean)

    def arrange(self):
        te = self.head
        tem = None
        if (self.head == None):
            return
        else:
            while (te != None):
                tem = te.next
                while (tem != None):
                    if (te.info > tem.info):
                        dup = te.info
                        te.info = tem.info
                        tem.info = dup
                    tem = tem.next
                te = te.next

    def Inverse(self):
        te = self.head
        tem = None

        if (self.head == None):
            return
        else:
            while (te != None):
                tem = te.next

                while (tem != None):
                    if (te.info < tem.info):
                        dup = te.info
                        te.info = tem.info
                        tem.info = dup
                    tem = tem.next
                te = te.next


slink = SinglyLinkedList()
alternative = True
while alternative is True:
    choice = Menu()
    if choice == 1:
        slink.Display()

    elif choice == 2:
        newinfo = int(input("Enter the Data: "))
        slink.place_beginning(newinfo)

    elif choice == 3:
        newinfo = int(input("Enter the Data: "))
        slink.place_end(newinfo)

    elif choice == 4:
        newinfo = int(input("Enter the Data: "))
        dis_node = int(input("Enter the Previous Node: "))
        slink.place_position(dis_node, newinfo)

    elif choice == 5:
        slink.delete_beginning()
        print("The List is: ")
        slink.Display()

    elif choice == 6:
        slink.delete_end()
        print("The List is: ")
        slink.Display()

    elif choice == 7:
        newinfo = int(input("Enter the Node: "))
        slink.delete_position(newinfo)
        print("The List is: ")
        slink.Display()

    elif choice == 8:
        slink.largest_node()

    elif choice == 9:
        slink.mean()

    elif choice == 10:
        slink.arrange()

    elif choice == 11:
        slink.Inverse()

    else:
        alternative = False

