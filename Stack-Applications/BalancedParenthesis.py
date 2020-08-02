from Stack import Stack

# sample example = {1+[(2*3)+5]}
sample = "{1+[(2*3)+5]}"

def VerifyExpression(sample):
    stack = Stack()

    for i in sample:
        print(f"current element => {i}")

        # check for open parenthesis
        if i == '{' or i == '[' or i == '(':
            stack.push(i)

        elif i == ')':
            if stack.peek() == '(':
                stack.pop()
            else:
                print("Not valid")
                return False
        elif i == ']':
            if stack.peek() == '[':
                stack.pop()
            else:
                return False
        elif i == '}':
            if stack.peek() == '{':
                stack.pop()
            else:
                return False
        print('-'*30)
        print("Current stack status")
        stack.Print()
        print('-'*30)
    
    if stack.peek() != -1:
        return False
    else:
        return True

print(VerifyExpression(sample))

while True:
    print("1: Testing again...")
    print("2: Exit")
    choice = int(input(">>>"))
    if choice == 1:
        string = input("Enter an expression with parenthensis: ")
        result = VerifyExpression(string)
        if result:
            print("Balanced | valid expression")
        else:
            print("Unbalanced | invalid expression")
    elif choice == 2:
        break