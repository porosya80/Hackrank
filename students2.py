if __name__ == '__main__':
    result = 0
    counter = 0
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    values = student_marks[query_name]
    for i in values:
        result += i
        counter += 1
    print ("{:.2f}".format(result /counter))