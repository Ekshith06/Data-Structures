""" Python Script to create a stack and perform various operations on it """
#by appened option we create a stacks

""" stacks are :: user defined functions
its operate in lifo order "last in first out"
two basic operation of stachs are:
push:add the element in the stack
pop:remove the element from the stack
in code language
push---->append
pop ---->pop
timecomplexity :
timecomplexity of pop is it just removes the top elwment  so ---->o(1)
timecomplexity of appened is it just adds the top elwment so ---->o(1)"""

#code

stack =[]
def push():
  element = input("enter the element:")
  stack.append(element)
  print(stack)
def remove():
  if not stack:
    print("stack is empty!")
  else:
    e = stack.pop()
    print("removed element:",e)
    print(stack)    
n = int(input("limit of the stack:"))    
while True:
  print("select the operation 1.push  2.pop  3.quit")
  choice = int(input())
  if choice==1:
    push()
  elif choice==2:
    pop_element()
  elif choice==3:
    break
  else:
    print("enter the correct operation")
    
"""
**
code in stack
1.stack  <=>  []  only list
2.push   <=>  st.appened(variable)  o(1)
3.pop    <=>  st.pop()              o(1)
4.top    <=>  st[-1]                o(1)   
5.empty  <=>  if len(st) ==0;empty  o(1)
6.size   <=>  len(st)               o(1)
"""
    
    
    
    
    
    
