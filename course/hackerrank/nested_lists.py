records = []
student = []

for pupil in range(int(input())):
    name = input()
    score = float(input())
    student.append(name)
    student.append(score)
    records.append(student)
    student = []

student_points = []

for student in records:
    student_points.append(student[1])

student_points = sorted(set(student_points), reverse=False)

alphabetical_order = []

for i in records:
    if i[1] == student_points[1]:
        alphabetical_order.append(i[0])

alphabetical_order = sorted(set(alphabetical_order), reverse=False)

for i in alphabetical_order:
    print(i)


