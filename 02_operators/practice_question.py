# Practice Questions on Operators

# 1️⃣ Even or Odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")


# 2️⃣ Positive, Negative, or Zero
num2 = int(input("Enter another number: "))
if num2 > 0:
    print("Positive")
elif num2 < 0:
    print("Negative")
else:
    print("Zero")


# 3️⃣ Maximum of two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("Maximum is:", a)
else:
    print("Maximum is:", b)


# 4️⃣ Check divisible by 5 and 3 (Logical AND)
n = int(input("Enter number to check divisibility by 5 and 3: "))

if n % 5 == 0 and n % 3 == 0:
    print("Divisible by both 5 and 3")
else:
    print("Not divisible by both 5 and 3")


# 5️⃣ Check divisible by 5 OR 3 (Logical OR)
n2 = int(input("Enter number to check divisibility by 5 or 3: "))

if n2 % 5 == 0 or n2 % 3 == 0:
    print("Divisible by 5 or 3")
else:
    print("Not divisible by 5 or 3")


# 6️⃣ Simple calculator using arithmetic operators
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print("Addition:", x + y)
print("Subtraction:", x - y)
print("Multiplication:", x * y)
print("Division:", x / y)
print("Remainder:", x % y)


# 7️⃣ Square and cube using power operator
n3 = int(input("Enter a number to find square and cube: "))
print("Square:", n3 ** 2)
print("Cube:", n3 ** 3)


# 8️⃣ Update marks using assignment operator
marks = int(input("Enter your marks: "))

marks += 5   # grace marks
print("Marks after grace:", marks)

marks -= 2   # penalty
print("Marks after penalty:", marks)
