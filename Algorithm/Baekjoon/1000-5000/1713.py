# import sys
# input = sys.stdin.readline
#
# n = int(input())
# total = int(input())
# array = list(map(int, input().split()))
#
# visited = [False] * (len(array) + 1)
#
# for i in range(len(array)):
#     if visited.count(True) != n:
#         visited[array[i]] = True
#     else:
#         if not visited[array[i]]:
#             visited[array[i - n]] = False
#             visited[array[i]] = True
#
# answer = []
# for i in range(len(visited)):
#     if visited[i]:
#         answer.append(i)
#
# print(*answer)

import sys
input = sys.stdin.readline

n = int(input())
num_student = int(input())
vote = list(map(int, input().split()))

student = [] # 사진틀에 게시된 학생 수
student_vote = [] # 사진틀에 게시된 학생의 추천 수

for v in vote:
    # 추천된 학생이 사진틀에 있는 경우
    if v in student:
        # 해당 학생 추천 수 증가
        idx = student.index(v)
        student_vote[idx] += 1
    else: # 추천된 학생이 사진틀에 없는 경우
        # 사진틀이 가득 찼다면
        if len(student) == n:
            # 추천수가 가장 적은 학생 제거
            idx = student_vote.index(min(student_vote))
            del student[idx]
            del student_vote[idx]
        # 사진틀이 가득 차지 않았다면 해당 학생 사진틀에 게시 후 투표수 증가
        student.append(v)
        student_vote.append(1)
    # print(student, student_vote)

student.sort()
print(*student)