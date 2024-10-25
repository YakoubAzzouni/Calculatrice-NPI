from typing import List

def evaluate_npi(expression: List[str]) -> float:
    stack = [] # une pile
    operators = {'+', '-', '*', '/'} #define the operators

    for element in expression: 
        if element not in operators:
            stack.append(float(element))
        else:
            b = stack.pop()
            a = stack.pop()
            if element == '+':
                stack.append(a + b)
            elif element == '-':
                stack.append(a - b)
            elif element == '*':
                stack.append(a * b)
            elif element == '/':
                if b == 0:
                    raise ValueError("Division by zero is not allowed.")
                stack.append(a / b)
    
    if len(stack) != 1:
        raise ValueError("Invalid expression.")
    
    return stack.pop()
