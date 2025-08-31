
student_score = input().split()
max_score = 0
for n in range(0, len(student_score)):
    student_score[n] = int(student_score[n])
    if max_score < student_score[n]:
        max_score = student_score[n]
print(max_score)