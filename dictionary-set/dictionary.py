# DICTIONARY PRACTICE – FULL CONCEPT

# Creating dictionary
student = {
    "name": "Mansi",
    "age": 20,
    "course": "Python",
    "marks": 85
}

print("Original Dictionary:", student)

# Accessing values
print("Name:", student["name"])
print("Marks using get():", student.get("marks"))

# Adding new key-value pair
student["city"] = "Ahmedabad"
print("After Adding City:", student)

# Updating value
student["marks"] = 90
print("After Updating Marks:", student)

# Removing element
removed_value = student.pop("age")
print("Removed Age:", removed_value)
print("After Removing Age:", student)

# Dictionary methods
print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())

# Length
print("Dictionary Length:", len(student))

# Looping through dictionary
print("Looping through dictionary:")
for key, value in student.items():
    print(key, ":", value)

# Nested Dictionary
students = {
    "student1": {"name": "Mansi", "marks": 90},
    "student2": {"name": "Riya", "marks": 85}
}

print("Nested Dictionary:", students)