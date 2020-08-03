class Queue():
    
    def __init__(self):
        # let's first start by defining the max size of the array
        self.MAX_SIZE = 10
        # initial conditions for empty queue 
        self.front = -1
        self.rear = -1

        self.q = [' ' for i in range(self.MAX_SIZE)]

    def IsFull(self):
        "determines whether the queue is empty or not"
        if self.rear == self.MAX_SIZE - 1:
            return True
        return False

    def IsEmpty(self):
        "determines whether the queue is empty or not"
        if self.front == -1 and self.rear == -1:
            return True
        else:
            return False
    
    def Enqueue(self,data):
        "ADDS A NEW ELEMENT IN QUEUE FROM REAR"
        if self.IsFull():
            print("Cannot enqueue as the queue is full")
            return
        elif self.IsEmpty():
            # increment both the pointers to point to first element
            self.front = self.rear = 0
        else:
            self.rear += 1    
        self.q[self.rear] = data
        

    def Dequeue(self):
        "REMOVES ELEMENT FROM FRONT 1 AT A TIME"
        # check if the queue is empty
        if self.IsEmpty():
            print("The queue is empty")
            return 
        # assign some value at the position which needs to be dequeued
        self.q[self.front] = ' '
        # increment the front pointer
        self.front += 1
    
    def Print(self):
        "PRINTS THE ENTIRE QUEUE IN PROPER HUMAN UNDERSTANDABLE FORMAT"
        print('-'*30)
        for i in range(self.MAX_SIZE):
            print(f"| {self.q[i]} |",end = '')
        print('')
        print('-'*30)
    
    @property
    def getFront(self):
        return self.front
    
    @property
    def getRear(self):
        return self.rear
        

def main():
    # create a queue instance
    queue = Queue()
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