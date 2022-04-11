"""
1부터 K 사이의 숫자를 하나 고르는 행위를 N번 반복하여 나올 수 있는 모든 서로 다른 순서쌍을 구해주는 프로그램을 작성해보세요.
단, 연속하여 같은 숫자가 3번 이상 나오는 경우는 제외합니다.

예를 들어 K이 2, N이 3인 경우 다음과 같이 6개의 조합이 가능합니다.

1 1 2

1 2 1

1 2 2

2 1 1

2 1 2

2 2 1
"""

# My
import sys
input = sys.stdin.readline

k, n = map(int, input().split())

answer = []
def choose():
    # n번 반복이 됐을 경우
    if len(answer) == n:
        flag = True
        count = 1
        # 연속된 수가 3개 이상인 경우를 검사
        for i in range(1, len(answer)):
            # 이전 값와 현재 값이 같다면 1 증가
            if answer[i] == answer[i - 1]:
                count += 1
            else: # 다르면 다시 1부터 시작
                count = 1

            # 연속된 값이 3개일 경우 탈출
            if count == 3:
                flag = False
                break

        # 조건에 맞는 조합만 출력
        if flag:
            print(*answer)

        return

    # 1 ~ k까지 가능한 모든 조합을 추출
    for i in range(1, k + 1):
        answer.append(i)
        choose()
        answer.pop()
    return

choose()

# Sol
# 변수 선언 및 입력
k, n = tuple(map(int, input().split()))
selected_nums = []


# 선택된 원소들을 출력해줍니다.
def print_permutation():
    for num in selected_nums:
        print(num, end=" ")
    print()


def find_duplicated_permutations(cnt):
    # n개를 모두 뽑은 경우 답을 출력해줍니다.
    if cnt == n:
        print_permutation()
        return

    for i in range(1, k + 1):
        if cnt >= 2 and i == selected_nums[-1] and \
                i == selected_nums[-2]:
            continue
        else:
            selected_nums.append(i)
            find_duplicated_permutations(cnt + 1)
            selected_nums.pop()


find_duplicated_permutations(0)