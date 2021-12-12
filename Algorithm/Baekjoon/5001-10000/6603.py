# 로또
# combinations으로 가능한 모든 조합 추출
import sys
from itertools import combinations

while True:
    array = list(map(int, sys.stdin.readline().split()))
    # 0이 입력되면 종료
    if array[0] == 0:
        break
    # 로또 번호 배열 추출
    nums = array[1:]
    # k개의 로또 번호 배열 중 6개의 번호를 뽑는 모든 조합
    result = list(combinations(nums, 6))
    # 형식에 맞춰 출력
    for i in range(len(result)):
        for j in range(len(result[i])):
            print(result[i][j], end=' ')
        print()
    print()

