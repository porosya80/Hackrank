from collections import namedtuple
count, student = int(input()), namedtuple('student', input())
students = [student(*input().split()) for i in range(count)]
print("{:.2f}".format(sum([int(student.MARKS) for student in students])/count))

