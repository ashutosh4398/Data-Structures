from Stack import Stack

def main():
    # create a new instance of stack for performing operations
    stack = Stack()
    while(True):
        print("1: Push")
        print("2: Pop")
        print("3: Peek")
        print("4: Print Stack")
        print("5: STOP")
        choice = int(input(">>>"))
        if choice == 1:
            element = int(input("Enter element to be inserted: "))
            stack.push(element)
        elif choice == 2:
            elem = stack.pop()
            print("Popped element: ", elem)
        elif choice == 3:
            elem = stack.peek()
            print("Element at top is: ",elem)
        elif choice == 4:
            stack.Print()
        else:
            break


if __name__ == '__main__':
    main()
