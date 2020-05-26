
def findPercentageOfStudent(students, studentName):
    if studentName not in students:
        return 0

    marks = students[studentName]
    totalMarks = 0

    for mark in marks:
        totalMarks+=mark

    return "{:.2f}".format(totalMarks/3)

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    print(findPercentageOfStudent(student_marks, query_name))
