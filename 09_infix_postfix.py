# Written by EKSHITH.KOLLA
# Date: 26/7/2021
# This Program is converts Infix to Postfix using Stack

class Postfix:
    def __init__(self,Infix):
        self.infix = Infix # Infix is Stored in this
        self.stack = []    # Initializing empty stack
        self.postfix = []  # The Resultant Postfix will be stored in this
        self.size=0

    def InfixtoPostfix(self):
        operators = ["^","*","/","+","-","="] # Operators
        op_precedence = {'^':1,'*':2, '/':2,'+':3, '-':3,'=':4} # Precedence of operators in Dictionary

        # Looping through each character
        for char in self.infix:
            if char == "(": # When "(" found will be appended to stack
                self.stack.append(char)
                self.size+=1
            
            elif char in operators: # If char is operator
                pre=op_precedence[char]
                # Only operators go in Stack
                if self.stack==[]: # if Stack is empty
                    self.stack.append(char) # Operator appends to Stack
                    self.size+=1
                
                else:
                    if self.stack[-1] == "(":



                        # if the Top element is "(" then
                        self.stack.append(char)
                        # operator must be appended since that operator is present inside the parenthesis
                        self.size+=1            # and will continue until ")" is found
                    
                    elif op_precedence[str(self.stack[-1])]<=pre: # if precedence of top of the Stack is 
                                                                # More than or equal to char precedence
                        for i in range(len(self.stack)): # Traversing till the size of the Stack
                            if self.stack[-1] == "(": # if the Top element is "(" then
                                self.stack.append(char) # operator must be appended since that operator is present inside the parenthesis
                                self.size+=1            # and will continue until ")" is found
                            if op_precedence[str(self.stack[-1])]<=pre: # After Top element is appended it again checks the condition
                                self.postfix.append(self.stack.pop()) # Top of the element appends to postfix because of Associativity if precedence is equal
                                self.size-=1                   # and if not eual then due to precedence    
                                if self.stack==[]:  # After appending if the Stack becomes empty
                                    self.stack.append(char) # Then char gets appended to Stack
                                    self.size+=1
                                if self.stack[-1] == "(": # if the Top element is "(" then
                                    self.stack.append(char) # operator must be appended since that operator is present inside the parenthesis
                                    self.size+=1            # and will continue until ")" is found
                                    break
                            
                            else: # if precedence of Top of the Stack is less than char precedence
                                self.stack.append(char) # Then char is appended to the Stack without removing the previous element
                                self.size+=1
                                if self.stack[-1] == "(": # if the Top element is "(" then
                                    self.stack.append(char) # operator must be appended since that operator is present inside the parenthesis
                                    self.size+=1            # and will continue until ")" is found
                                    break
                        
                    else: # if precedence of Top of the Stack is less than char precedence
                        self.stack.append(char) # Then char is appended to the Stack without removing the previous element
                        self.size+=1
            
            elif char == ")": # When ")" found every element till "(" will be popped in the Stack
                for i in range(self.size):
                    if self.stack[-1] == "(": # Loop breaks when top is "("
                        self.stack.pop()
                        break
                    else:
                        self.postfix.append(self.stack.pop())
            
            else: # If it is operands,they would be directly appended
                self.postfix.append(char)
        
        for i in range(self.size):
            if self.stack==[]:
                break
            self.postfix.append(self.stack.pop()) # if any operators are present they would be appended to the postfix

    def printPostfix(self):
        print("The Postfix of ",self.infix," is: ",end="")
        for char in self.postfix:
            print(char,end="")
        print()

# Driver Code
if __name__ == "__main__":
    Infix = str(input("Enter the Infix: "))
    ip = Postfix(Infix)
    ip.InfixtoPostfix()
    ip.printPostfix()
# End of the Program
