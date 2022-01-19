# 시간 초과
import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))
array.sort()
avg = int(sum(array) / len(array))

answer = []
v = 1e9
for i in range(len(array)-1, -1, -1):
    if array[i] > avg:
        continue
    tmp = 0
    for j in range(len(array)):
        tmp += abs(array[i] - array[j])

    if tmp <= v:
        answer.append(array[i])
        v = tmp

print(min(answer))


# divmod 이용하면 가운데 인덱스를 구하고 중앙값에 접근
import sys
input = sys.stdin.readline

n = int(input())
# 배열 입력받은 후 정렬
array = list(map(int, input().split()))
array.sort()

# 몫과 나머지 구하기
q, r = divmod(n, 2)
# 목과 나머지를 이용하여 인덱스를 구한 뒤 중앙값에 접근
print(array[q+r-1])
