class Node():
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

def get_new_node(x):
    node = Node(x)
    return node

def insert_at_head(value,head):
    "INSERTS NEW NODE AT 0TH POSITION / HEAD "
    node = get_new_node(value)
    if head == None:
        head = node
    else:
        head.prev = node
        node.next = head
        head = node
    return head

def insert_at_tail(value,head):
    "INSERTS NEW NODE AT THE END OF LIST"
    node = get_new_node(value)
    if head == None:
        head = node
    else:
        # need to traverse the entire list
        temp = head
        while(temp.next != None):
            temp = temp.next
        temp.next = node
        node.prev = temp
    return head

def insert_at_n(value,pos,head):
    "INSERTS A NEW NODE AT NTH POSITION"
    count = 0
    temp = head
    while(count != pos and temp):
        print(temp.data,count)
        count += 1
        temp = temp.next
    node = get_new_node(value)
    node.prev = temp.prev
    node.next = temp
    temp.prev.next = node
    temp.prev = node
    return head

def delete_at_n(pos,head):
    count = 0
    temp = head
    while(pos != count and temp):
        temp = temp.next
        count += 1
    # deletion
    temp.prev.next = temp.next
    temp.next.prev = temp.prev
    return head

def PrintForward(head):
    temp = head
    while(temp):
        print(f"[{temp.data}] --> ",end='')
        temp = temp.next
    print("NULL")

def PrintBackward(head):
    temp = head
    while(temp and temp.next):
        # traverse till the last node
        temp = temp.next
    # now start from the last node and print values till the head
    while(temp):
        print(f"[{temp.data}] --> ",end='')
        temp = temp.prev
    print("NULL")

def main():
    head = None # initial value of head
    while True:
        print("1: Insert at head")
        print("2: Insert at tail")
        print("3: Insert at nth position")
        print("4: Delete at nth position")
        print("5: Print forward direction")
        print("6: Backward direction")
        print("7: Exit")
        choice = int(input(">>>"))
        if choice == 1:
            value = int(input("Enter value to be inserted: "))
            head = insert_at_head(value,head)
        elif choice == 2:
            value = int(input("Enter value to be inserted: "))
            head = insert_at_tail(value,head)
        elif choice == 3:
            pos = int(input("Enter the position at which new element is to be inserted: "))
            value = int(input("Enter the value to be inserted: "))
            head = insert_at_n(value,pos,head)
            PrintForward(head)
        elif choice == 4:
            pos = int(input("Enter the position to be deleted: "))
            head = delete_at_n(pos,head)
        elif choice == 5:
            PrintForward(head)
        elif choice == 6:
            PrintBackward(head)
        else:
            break

if __name__ == '__main__':
    main()