# 2108
# 1, 테이블 만들어 순회하면 최빈값 찾기 - 1652ms
import sys
from collections import Counter

n = int(sys.stdin.readline())
array = []
for i in range(n):
    array.append(int(sys.stdin.readline()))

# 1. 산술 평균
print(round(sum(array) / n))

# 2. 중앙값
array.sort()
print(array[n // 2])

# 3. 최빈값
# -4000 ~ 4000까지의 빈도수를 저장할 테이블
d = [0] * 8001
# 배열을 순회하며
for i in array:
    # 배열의 요소가 0보다 크면
    if i >= 0:
        # index 0~4000에 추가
        d[i] += 1
    # 0보다 작으면
    else:
        # index 4001~8000에 추가
        d[4000 - i] += 1

result = []

# 빈도수를 저장한 배열을 순회
for i in range(len(d)):
    # 여기서 i는 인덱스가 아닌 숫자와 동일
    # 빈도수가 최대값과 같을 경우
    if d[i] == max(d):
        # i가 4000보다 크면 음수로 만들어주고 추가
        if i > 4000:
            result.append(-(i - 4000))
        else:
            result.append(i)
result.sort()

if len(result) > 1:
    print(result[1])
else:
    print(result[0])

# 4. 범위
print(max(array) - min(array))

# 2, Counter 모듈 이용 - 720ms
n = int(sys.stdin.readline())
array = []
for i in range(n):
    array.append(int(sys.stdin.readline()))

# 1. 산술 평균
print(round(sum(array) / n))

# 2. 중앙값
array.sort()
print(array[n // 2])

# 3. 최빈값
count = Counter(array).most_common()
if len(count) > 1 and count[0][1] == count[1][1]:
    print(count[1][0])
else:
    print(count[0][0])

# 4. 범위
print(max(array) - min(array))