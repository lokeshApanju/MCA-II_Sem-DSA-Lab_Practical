# Program to Evaluate Postfix Expression Using Stack

def evaluate_postfix(expression):
    stack = []
    tokens = expression.split()

    for token in tokens:
        if token.lstrip('-').isdigit():
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(int(a / b))

    return stack[0]


print("=== Postfix Expression Evaluator ===")
print("Enter tokens separated by spaces (e.g., 3 4 + 2 * )")
expr = input("Enter postfix expression: ")

result = evaluate_postfix(expr)
print("Result:", result)

