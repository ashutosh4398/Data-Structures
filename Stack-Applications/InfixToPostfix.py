from Stack import Stack

operators = ['+','-','*','/','^']
def get_precedence(operator):
    "FUNCTION TO DECIDE OPERATOR PRECEDENCE"
    if operator == '+' or operator == '-':
        return 1
    elif operator == '*' or operator == '/':
        return 2
    elif operator == '^':
        return 3
    else:
        return -1

def InfixToPostfix(expression):
    stack = Stack()
    res = ''
    i = 0
    while i < len(expression):
        if expression[i] == '(':
            stack.push(expression[i])
        elif expression[i] in operators:
            if stack.peek() == '(':
                stack.push(expression[i])  
            elif get_precedence(expression[i]) > get_precedence(stack.peek()):
                stack.push(expression[i])
            else:
                while get_precedence(expression[i]) <= get_precedence(stack.peek()) and expression[i] in operators:
                    res += stack.pop()
                stack.push(expression[i])
        elif expression[i] == ')':
            while stack.peek() != '(':
                res += stack.pop()
            stack.pop()
        else:
            res += expression[i]
        
        print(res)
        i += 1
        stack.Print()
        print('-'*30)

    while stack.peek() != -1:
        res += stack.pop()
    return res

expression = '((A+B)*C-D)*E'
print(InfixToPostfix(expression))