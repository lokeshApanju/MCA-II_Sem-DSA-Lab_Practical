# Program to Demonstrate Recursion Using Stack

def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)


def factorial_using_stack(n):
    stack = []
    result = 1

    while n > 1:
        stack.append(n)
        n -= 1

    print("Stack frames (top to bottom):", stack[::-1])

    while stack:
        result *= stack.pop()

    return result

print("=== Recursion Demo: Factorial ===")
num = int(input("Enter a number: "))

print("\n-- Using Recursion --")
print(f"Factorial of {num} =", factorial_recursive(num))

print("\n-- Using Manual Stack --")
print(f"Factorial of {num} =", factorial_using_stack(num))

