student_height = input().split()

for n in range(0, len(student_height)):
    student_height[n] = int(student_height[n])
height = 0
for m in student_height:
    height += m
students = len(student_height)
avg = height/students
print(f'total height = {height}')
print(f"number of students = {students}")
print(f"average height = {avg}")
