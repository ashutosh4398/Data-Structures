"HERE WE HAVE ASSUMED THAT ALL THE INPUT STRINGS ARE VALID AND ONLY CONTAINS DIGITS [0-9]"
from Stack import Stack

operators = ['+','-','*','/','^']

def evaluatePostfix(expression):
    """
        In postfix expression, we start scanning the expression from left to right
    """
    stack = Stack()
    for i in expression:
        # check if the current character is an operator or digit
        if i in operators:
            # perform the operation
            op2 = int(stack.pop())
            op1 = int(stack.pop())
            if i == '+':
                res = op1 + op2
            elif i == '-':
                res = op1 - op2
            elif i == '*':
                res = op1 * op2
            elif i == '/':
                res = op1 / op2
            elif i == '^':
                res = op1 ** op2
            # push the result into the stack
            stack.push(res)
        else:
            stack.push(i)
        stack.Print()
        print('-'* 30)
    # return the element left in stack
    return stack.peek()

sample = input("Enter a valid postfix expression: ")
result = evaluatePostfix(expression = sample)
print(f"The result is {result}")