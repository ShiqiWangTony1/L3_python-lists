# Task 1: Given the list of grades:
# grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
# sort_grade = sorted(grades)[::-1]
# print(sort_grade)

# Task 2: Calculate the average grade and display it.
# avg_grade = sum(grades) / len(grades)
# print(avg_grade)

# Task 3: Replace any grade below 80 with the value Failed.
# replace_grade = ["Failed" if grade < 80 else grade for grade in grades]
# print("The replace grades version grades list is",replace_grade)

# 2.
# Task 1: Given the two lists
# submitted = ["Alice", "Bob", "Charlie", "David"]
# attended = ["Charlie", "Eve", "Alice", "Frank"]
# both_students = []
# for student in submitted:
#     if student in attended:
#         both_students.append(student)
# print(both_students)

# Task 2: Check if the two lists are identical in terms of their content, regardless of order.
# if sorted(submitted) == sorted(attended):
#     answer = True
# else:
#     answer = False
# print("The two lists are identical?", answer)

# Task 3: 
# attended = [student for student in attended if student in submitted]
# print(attended)

# 3.
# Task 1
# temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]
# second_week_temp = temperatures[7:14]
# print(second_week_temp)

# Task 2
# temp_above_100 = [temp for temp in temperatures if temp > 100]
# print(temp_above_100)

# Task 3
# reverse_temp = temperatures[::-1]
# fifth_to_10th = reverse_temp[4:10]
# print(fifth_to_10th)


# 4. 
# Task 1
# students = ["John", "Doe", "Jane", "Smith"]
# grades = [85, 90, 78, 88]
# activities = ["Football", "Music", "Art", "Dance"]

# for student, grade, activity in zip(students, grades, activities):
#     if grade < 80:
#         print(f"{student}, {grade}, {activity}")

# Task 2
# students_approved = []

# for student, grade in zip(students, grades):
#     if grade >= 80:
#         students_approved.append(student)

## Task 3
# print("students_approved:", students_approved)
