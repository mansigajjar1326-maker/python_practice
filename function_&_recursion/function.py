# Functions Practice

print("=== Functions Practice ===\n")

# 1️⃣ Simple function
def greet():
    print("Hello, welcome to Python learning!")

greet()


# 2️⃣ Function with parameters
def add_numbers(a, b):
    result = a + b
    return result

sum_result = add_numbers(5, 3)
print("Sum:", sum_result)


# 3️⃣ Function with default parameter
def greet_user(name="Guest"):
    print("Hello,", name)

greet_user("Mansi")
greet_user()


# 4️⃣ Even or Odd using function
def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

print("10 is", check_even_odd(10))


# 5️⃣ Maximum of two numbers
def find_max(a, b):
    if a > b:
        return a
    else:
        return b

print("Maximum number is:", find_max(15, 9))