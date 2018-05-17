
if __name__ == '__main__':
    students = {}
    for i in range(int(input())):
        name = input()
        score = float(input())
        if score in students:
            students[score].append(name)
        else:
            students[score] = [name]
    scores = list(students.keys())
    scores.sort()
    for i in sorted(students[scores[1]]):
        print (i)

    # print(students)