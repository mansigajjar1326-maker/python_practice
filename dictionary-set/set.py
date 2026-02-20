# SET PRACTICE – CLEAN VERSION

# Creating set (duplicates automatically removed)
numbers = {10, 20, 30, 40, 40, 50}
print("Original Set:", numbers)

# Adding element
numbers.add(60)
print("After Add:", numbers)

# Removing element safely
if 20 in numbers:
    numbers.remove(20)

print("After Remove:", numbers)

# Discard (safe remove, no error if not present)
numbers.discard(100)
print("After Discard:", numbers)

# Length
print("Set Length:", len(numbers))

# Membership check
print("Is 30 in set?", 30 in numbers)

# Looping through set
print("Looping through set:")
for num in numbers:
    print(num)

# Set Operations
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print("Union:", a.union(b))
print("Intersection:", a.intersection(b))
print("Difference (a - b):", a.difference(b))
print("Symmetric Difference:", a.symmetric_difference(b))

# Converting list to set
list_numbers = [1, 2, 2, 3, 4]
unique_numbers = set(list_numbers)
print("Unique numbers from list:", unique_numbers)