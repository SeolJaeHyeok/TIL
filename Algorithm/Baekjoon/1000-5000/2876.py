import sys
input = sys.stdin.readline

n = int(input())

grades = [[0] * 6 for _ in range(n + 1)]

max_student = 0
grade = 1e9
for i in range(1, n + 1):
    a, b = map(int, input().split())

    # a에 대해서 먼저 처리
    # i번째 책상까지 a 그레이드를 받은 학생 수는 i - 1번째까지 책상까지 a라는 그레이드를 받은 학생 수 +1
    grades[i][a] = grades[i - 1][a] + 1 # 이전까지의 값 +1

    # i번째 책상까지 a 그레이드를 받은 학생이 최대 학생수보다 클 경우 최대 학생수와 갱신하고 해당 그레이드로 변경
    if grades[i][a] > max_student:
        max_student = grades[i][a]
        grade = a

    # a와 b가 다를 경우 b에 대해서 같은 처리
    if a != b:
        grades[i][b] = grades[i - 1][b] + 1
        if grades[i][b] > max_student:
            max_student = grades[i][b]
            grade = b

# 해당 그레이드를 받은 최대 학생 수가 동일한 경우 더 작은 그레이드로 설정
min_grade = 1e9
for i in range(1, n + 1):
    for j in range(6):
        if grades[i][j] == max_student:
            min_grade = min(min_grade, j)

print(max_student, min_grade)