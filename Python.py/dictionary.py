# Creating a dictionary
student = {
    "name": "Alice",
    "age": 20,
    "course": "BCA"
}

# Accessing values
print("Name:", student["name"])
print("Age:", student["age"])

# Adding a new key-value pair
student["grade"] = "A"
print("Updated dictionary:", student)

# Modifying a value
student["age"] = 21
print("Modified age:", student)

# Removing a key-value pair
del student["course"]
print("After deletion:", student)

# Looping through dictionary
for key, value in student.items():
    print(key, ":", value)
