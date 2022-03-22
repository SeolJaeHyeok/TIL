import sys
input = sys.stdin.readline

n = int(input())

array = []
for _ in range(n):
    array.append(int(input()))

array.sort()

count = 0
flag = 1 # 단계별 최대 명예점수
# 명예 점수가 낮은 사람부터 끌어내리기
for i in range(len(array)):
    # 명예 점수가 최대 명예점수보다 크다면 차이만큼 결과값에 더하고
    if array[i] >= flag:
        count += array[i] - flag
        flag += 1 # 단계 증가

print(count)

