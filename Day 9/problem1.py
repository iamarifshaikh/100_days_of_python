studentScores = {
  "Arif": 80,
  "Atharva": 83,
  "Pratej": 75,
  "Anas": 88,
  "Danish": 83,
  "Rahul": 65
}

studentGrades = {}

for student in studentScores:
  score = studentScores[student]
  if score > 90:
    studentGrades[student] = "Outstanding"
  elif score > 80:
    studentGrades[student] = "Exceeds Expectations"
  elif score > 70:
    studentGrades[student] = "Average"
  elif score > 60:
    studentGrades[student] = "You need to do hardwork"
  else:
    studentGrades[student] = "Youre failed"

print(studentGrades)