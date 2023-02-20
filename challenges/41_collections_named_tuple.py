from collections import namedtuple
N = int(input())
fields = input().split()
Student_Result = namedtuple('student_result', fields)
total_marks = 0
for _ in range(N):
    result = input().split()
    student = Student_Result(*result)
    total_marks += int(student.MARKS)

print('{:.2f}'.format(total_marks / N))