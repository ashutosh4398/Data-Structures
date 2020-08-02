"""
    Linked List reversal using explict stack
    implict stack can be achieved by making use of recursive calls
"""


from Stack import Stack

class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

def insert(value,head):
    "INSERTS ELEMENTS AT THE END OF LINKED LIST"
    node = Node(value)
    if head == None:
        head = node
    else:
        # traverse till the end
        temp = head
        while(temp.next):
            temp = temp.next
        temp.next = node
    return head

def Print(head):
    "PRINTS ALL THE ELEMENTS OF LINKED LIST"
    temp = head
    while(temp):
        print(f"[{temp.data}]-->",end='')
        temp = temp.next
    print("NULL")

def ReverseLinkedL(head):
    "REVERSES THE LINKED LIST USING EXPLICIT STACK IMPLEMENTATION"
    # creating the stack instance
    stack = Stack()
    temp = head
    while(temp):
        # keep on pushing all the stack elements
        stack.push(temp)
        temp = temp.next
    # now we need to pop the elements from stack for reversal and adjust the links
    # pop the first element and mark it as new head
    head = stack.pop()
    temp = head
    while(stack.peek() != -1):
        temp.next = stack.pop()
        temp = temp.next
    # adjusting the last element
    temp.next = None
    return head

head = None
print("creating a new linked list....")
print("Enter -1 at end")
while True:
    value = int(input("Enter element: "))
    if value == -1:
        break
    else:
        head = insert(value,head)

print("Your linked list")
Print(head)
print("Linked list reversal begins......")
head = ReverseLinkedL(head)
print("After reversal...")
Print(head)
