student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
new_student_score ={}


for key, value in student_scores.items():
    if value >= 91:
        new_student_score[key]= "Outstanding"
    elif value >= 81:
        new_student_score[key] = "Exceeds Expectations"
    elif value >= 71:
        new_student_score[key] = "Acceptable"
    else:
        new_student_score[key] = "Fail"

print(new_student_score)