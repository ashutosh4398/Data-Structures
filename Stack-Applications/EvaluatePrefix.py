"HERE WE HAVE ASSUMED THAT ALL THE INPUT STRINGS ARE VALID AND ONLY CONTAINS DIGITS [0-9]"
from Stack import Stack

operators = ['+','-','*','/','^']

def evaluatePrefix(expression):
    # create a new stack
    stack = Stack()
    # here in this case, we have to start scanning the expression from right
    for i in expression[::-1]:
        if i in operators:
            op1 = int(stack.pop())
            op2 = int(stack.pop())
            if i == '+':
                res = op1 + op2
            elif i == '-':
                res = op1 - op2
            elif i == '*':
                res = op1 * op2
            elif i == '/':
                res = op1 / op2
            elif i == '^':
                res = op1 ^ op2
            stack.push(res)
        else:
            stack.push(i)
        stack.Print()
        print('-'*30)
    
    return stack.peek()


expression = input("Please enter a valid prefix expression: ")

result = evaluatePrefix(expression)
print(result)