student_height = input("Enter the heights of all students: ").split()

for h in range(0, len(student_height)):
    student_height[h] = int(student_height[h])

print(student_height)

total_height = 0
 
for height in student_height:
    total_height += height
print(total_height)

total_student = 0

for student in student_height:
    total_student += 1
print(total_student)

average_height = str(round(total_height / total_student))

print("The average height of a student in class is " + average_height + " cm")
