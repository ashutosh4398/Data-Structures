class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

# marks as the start of node / represents the linked list
head = None
print("Creating a linked list.....")
print("Enter elements and -1 at end: ")

def printList(head):
    "PRINTS THE ENTIRE LINKED LIST"
    temp = head
    while(temp):
        print(f"[{temp.data}] --> ",end='')
        temp = temp.next
    print('NULL')

def Insert(x,head):
    "INSERT ELEMENTS AT THE BEGINNING OF LIST"
    node = Node(x)
    node.data = x
    node.next = head
    head = node
    return head

def InsertAtN(pos,value,head):
    "INSERTS ELEMENTS AT NTH POSITION"
    count = 0
    # this line is written just to stick with the convention of not using the head directly
    temp = head
    # keep track of previous node as well
    prev = head
    while count != pos and temp:
        count += 1
        prev = temp
        temp = temp.next
    new_node = Node(value)
    new_node.data = value
    new_node.next = temp
    prev.next = new_node

def DeleteAtN(pos,head):
    "DELETES A NODE AT NTH POSITION"
    if pos == 0:
        return head.next
    count = 0
    temp = head
    prev = head
    while count != pos and temp:
        count += 1
        prev = temp
        temp = temp.next
    # once we found the accurate position then just delete
    prev.next = temp.next
    del temp
    return head

def ReverseLinkedListIterative(head):
    temp = head
    prev = None
    while(temp):
        var = temp.next
        temp.next = prev
        prev = temp
        temp = var
    return prev
    
def ReverseLinkedListRecursive(current):
    "REVERSES A LINKED LIST USING RECURSION"
    if current.next == None:
        # last node
        return current
    
    head = ReverseLinkedListRecursive(current.next)
    temp = current.next
    current.next = None
    temp.next = current
    return head

while(True):
    print("0: STOP")
    print("1: Printing the linked list")
    print("2: Insert at beginning")
    print("3: Insert at nth position")
    print("4: Delete a node at nth position")
    print("5: Reverse a linked list using iterative method")
    print("6: Reverse a linked list using Recursive method")
    choice = int(input(">>>"))
    if choice == 1:
        printList(head)
    elif choice == 2:
        x = int(input("Enter value: "))
        head = Insert(x,head)
    elif choice == 3:
        pos = int(input("Enter pos at which you want to insert the new node: "))
        value = int(input("Enter value to be entered: "))
        InsertAtN(pos,value,head)
    elif choice == 4:
        pos = int(input("Enter position of node to be deleted: "))
        head = DeleteAtN(pos,head)
        print("Deleted successfully....")
    elif choice == 5:
        head = ReverseLinkedListIterative(head)
        printList(head)
    elif choice == 6:
        head = ReverseLinkedListRecursive(head)
        printList(head)
    elif choice == 0:
        break