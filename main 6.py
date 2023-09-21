def sort_students(student_list):
    # Sort the student list based on CGPA in descending order
    sorted_students = sorted(student_list, key=lambda student: student['cgpa'], reverse=True)
    return sorted_students

# Define a list of student objects for testing
students = [
    {'name': 'Alice', 'roll_number': 'A001', 'cgpa': 3.8},
    {'name': 'Bob', 'roll_number': 'B002', 'cgpa': 3.5},
    {'name': 'Charlie', 'roll_number': 'C003', 'cgpa': 3.9},
    {'name': 'David', 'roll_number': 'D004', 'cgpa': 3.7},
]

# Call the function to sort the students
sorted_students = sort_students(students)

# Print the sorted list
for student in sorted_students:
    print(f"Name: {student['name']}, Roll Number: {student['roll_number']}, CGPA: {student['cgpa']}")
