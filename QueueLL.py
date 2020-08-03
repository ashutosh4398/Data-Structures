class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None
    
    def Insert(self,x,rear):
        "INSERT AT END"
        node = Node(x)
        if self.head == None:
            self.head = node

        if rear == None:
            self.head = node
            return self.head
        else:
            rear.next = node
            rear = node
            return rear
    
    def Delete(self,front):
        if front == None:
            return None
        else:
            return front.next

    def Print(self):
        temp = self.head
        while(temp):
            print(f"| {temp.data} |",end='')
            temp = temp.next
        print()


class Queue():
    def __init__(self):
        self.front = None
        self.rear = None
        self.q = LinkedList()
    
    def IsEmpty(self):
        if self.front == None and self.rear == None:
            return True
        return False
    
    def Enqueue(self,value):
        if self.IsEmpty():
            self.front = self.rear = self.q.Insert(value,self.rear)
        else:
            self.rear = self.q.Insert(value,self.rear)
    
    def Dequeue(self):
        if self.IsEmpty():
            return
        elif self.front == self.rear:
            self.front.data = ' '
            self.front = self.rear = None
        else:
            self.front.data = ' '
            self.front = self.q.Delete(self.front)

    @property
    def getFront(self):
        if self.front:
            return self.front.data
    
    @property
    def getRear(self):
        if self.rear:
            return self.rear.data
    
    def Print(self):
        self.q.Print()

    
def main():
    queue = Queue()
    while(True):
        print("1: Enqueue")
        print("2: Dequeue")
        print("3: IsEmpty")
        print("4: Print the entire queue")
        print("5: Current value of front")
        print("6: Current value of rear")
        print("7: STOP")
        choice = int(input(">>>"))
        if choice == 1:
            data = int(input("Enter the value to be entered: "))
            queue.Enqueue(data)
        elif choice == 2:
            queue.Dequeue()
        elif choice == 3:
            status = queue.IsEmpty()
            if status:
                print("Queue is Empty")
            else:
                print("Queue is not empty")
        elif choice == 4:
            queue.Print()
        elif choice == 5:
            print(f"The current value at front is: {queue.getFront}")
        elif choice == 6:
            print(f"The current value at rear is: {queue.getRear}")
        else:
            break

if __name__ == '__main__':
    main()