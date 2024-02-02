n = int(input())
student_marks = {}

for i in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()

# for key, value in student_marks:
#     print(key, value)


avg_score = sum(student_marks[query_name]) / len(student_marks[query_name])
print(f'{avg_score:.2f}')




