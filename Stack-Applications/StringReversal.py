from Stack import Stack

def main():
    while True:
        print("1: Reverse a string")
        print("2: Stop")
        choice = int(input(">>>"))
        if choice == 1:
            string = input("Enter a valid string: ")
            # creating a new stack instance
            stack = Stack()
            # push elements of string in stack
            for i in range(len(string)):
                stack.push(string[i])
            # print the filled stack
            stack.Print()

            # since stack is LIFO structure, we will start popping the last elements from top
            newstring = ''
            for i in range(len(string)):
                newstring += stack.pop()

            # freeeing the stack 
            del stack
            print(newstring)
        else:
            break

if __name__ == '__main__':
    main()