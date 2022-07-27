""" Python Script to create a queue and perform various operations on it """

# Write your code from here
""" queue is similar to stacks
it is also user defined func
here we have "FIFO" or "LILO"
oueue using list:
q.enqueue  <=> list.appened    o(1)
q.dequeue  <=> list.pop        o(1)   
q.front    <=> list.index[0]   o(1)
q.rear     <=> list[-1]        o(1)   
"""
#122010322044
#ekshit kolla
queue =[]
def enqueue():
  element = input("enter the element:")
  queue.append(element)
  print(element)
  
def dequeue():
  if not queue:
    print("queue is empty!")
  else:
    e = queue.pop(0)
    print("removed element:",e)
    
def display():
  print(queue)

  
while True:
  print("select the operation 1.add  2.remove  3.show  4.quit")
  choice = int(input())
  if choice==1:
    enqueue()
  elif choice==2:
    dequeue()
  elif choice==3:
    display()
  elif choice==4:
    break
  else:
    print("enter the correct operation")


