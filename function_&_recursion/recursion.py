# Recursion Practice

print("=== Recursion Practice ===\n")

# 1️⃣ Factorial using recursion
def factorial(n):
    if n == 0 or n == 1:   # Base case
        return 1
    else:
        return n * factorial(n - 1)   # Recursive call

print("Factorial of 5:", factorial(5))


# 2️⃣ Sum of first n natural numbers
def sum_natural(n):
    if n == 1:
        return 1
    else:
        return n + sum_natural(n - 1)

print("Sum of first 5 natural numbers:", sum_natural(5))


# 3️⃣ Fibonacci using recursion
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print("Fibonacci of 6:", fibonacci(6))