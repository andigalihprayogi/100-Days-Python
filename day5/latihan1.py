student_hieght = input("input student height :").split()
total_hieght = 0
for n in range(0, len(student_hieght)):
    student_hieght[n] = int(student_hieght[n])
    total_hieght += student_hieght[n]


print(f"total height ={total_hieght}")
print(f"number of student ={len(student_hieght)}")
print(f"average height = {total_hieght/len(student_hieght)}")
