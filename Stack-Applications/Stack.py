"""
The main aim of operations of stack ie push() and pop() is to execure in O(1) time ie
constant time.
In linked list, inserting and deleting an element at the end requires traversing the
entire linked list which would result in O(n) complexity
So for we insert and delete elements from start/head of the linked list which takes
constant time O(1)
"""

class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack():
    def __init__(self):
        self.top = None # acts as head ptr.
    
    def push(self,value):
        node = Node(value)
        if self.top == None:
            self.top = node
        else:
            node.next = self.top
            self.top = node
    
    def Print(self):
        temp = self.top
        while(temp):
            print('|' , temp.data , '|')
            print('------')
            temp = temp.next
    
    def peek(self):
        if self.top:
            return self.top.data
        else:
            print("Stack is empty")
            return -1
    
    def pop(self):
        if self.top == None:
            print("Stack underflow")
            return -1
        else:
            temp = self.top
            self.top = self.top.next
            return temp.data
