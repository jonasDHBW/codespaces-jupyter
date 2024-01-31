import random

def generate_student():
    first_names = ["John", "Jane", "Alice", "Bob", "Charlie", "David", "Emma", "Frank", "Grace", "Henry"]
    last_names = ["Smith", "Johnson", "Williams", "Jones", "Brown", "Miller", "Davis", "Garcia", "Rodriguez", "Martinez"]
    
    student = {
        "first_name": random.choice(first_names),
        "last_name": random.choice(last_names),
        "age": random.randint(18, 25),
        "grade": random.randint(1, 12)
    }
    
    return student

# Generate a list of students
num_students = 10
students = [generate_student() for _ in range(num_students)]

# Print student information
for i, student in enumerate(students, start=1):
    print(f"Student {i}: {student['first_name']} {student['last_name']}, Age: {student['age']}, Grade: {student['grade']}")

# Create a list of first names
first_names_list = [student["first_name"] for student in students]

# Use sets to find duplicates and print them
duplicates = {name: first_names_list.count(name) for name in set(first_names_list) if first_names_list.count(name) > 1}
if duplicates:
    print(f"\nDuplicate first names: {first_names_list}")
    print(duplicates)
else:
    print("\nNo duplicate first names.")
