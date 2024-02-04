student_scores = input("Enter the scores of the students: \n").split()

for marks in range(0, len(student_scores)):
  student_scores[marks] = int(student_scores[marks])

print(student_scores)

max_score = 0

for score in student_scores:
  if score > max_score:
    max_score = score

print(f"The Highest Score In The Class Is {max_score}")