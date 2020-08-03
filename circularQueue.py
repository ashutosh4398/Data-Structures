class CircularQueue():
    def __init__(self):
        # setting the max size of the queue
        self.MAX_SIZE = 10
        # initial conditions for empty queue
        self.front = -1
        self.rear = -1
        # creating an empty queue
        self.q = [' ' for i in range(self.MAX_SIZE)]
    
    def IsFull(self):
        if (self.rear + 1) % self.MAX_SIZE == self.front:
            return True
        return False

    def IsEmpty(self):
        if self.front == -1 and self.rear == -1:
            return True
        return False

    def Print(self):
        "PRINTS THE ENTIRE QUEUE IN HUMAN READABLE FORM"
        for i in range(self.MAX_SIZE):
            print(f"| {self.q[i]} ",end='')
        print('|')

    def Enqueue(self,data):
        if self.IsFull():
            print("QUEUE IS FULL")
            return 
        elif self.IsEmpty():
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.MAX_SIZE
        self.q[self.rear] = data

    def Dequeue(self):
        if self.IsEmpty():
            print("QUEUE UNDERFLOW")
            return
        elif self.front == self.rear:
            # if there is only a single element in queue
            self.q[self.front] = ' '
            self.front = self.rear = -1
        else:
            self.q[self.front] = ' '
            self.front = (self.front + 1) % self.MAX_SIZE

    @property
    def getFront(self):
        return self.front
    
    @property
    def getRear(self):
        return self.rear


def main():
    queue = CircularQueue()
    print(dir(queue))
    while(True):
        print("1: Enqueue")
        print("2: Dequeue")
        print("3: IsFull")
        print("4: IsEmpty")
        print("5: Print the entire queue")
        print("6: Current value of front")
        print("7: Current value of rear")
        print("8: STOP")
        choice = int(input(">>>"))
        if choice == 1:
            data = int(input("Enter the value to be entered: "))
            queue.Enqueue(data)
        elif choice == 2:
            queue.Dequeue()
        elif choice == 3:
            status = queue.IsFull()
            if status:
                print("Queue is FULL")
            else:
                print("Queue is NOT FULL")
        elif choice == 4:
            status = queue.IsEmpty()
            if status:
                print("Queue is Empty")
            else:
                print("Queue is not empty")
        elif choice == 5:
            queue.Print()
        elif choice == 6:
            print(f"The current value of front is: {queue.getFront}")
        elif choice == 7:
            print(f"The current value of rear is: {queue.getRear}")
        else:
            break

if __name__ == '__main__':
    main()