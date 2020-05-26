from typing import List


def findStudentSecondLowestGrade(students: List):
    lowest = 9999999999
    secondLowest = 0
    nameList = []
    for student in students:
        score = student[1]
        if lowest > score:
            secondLowest = lowest
            lowest = score
        elif lowest != score and secondLowest > score:
            secondLowest = score
    for student in students:
        name = student[0]
        score = student[1]
        if score == secondLowest:
            nameList.append(name)

    nameList.sort()
    for name in nameList:
        print(name)

if __name__ == '__main__':
    studentList = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        studentList.append([name, score])
    findStudentSecondLowestGrade(studentList)
