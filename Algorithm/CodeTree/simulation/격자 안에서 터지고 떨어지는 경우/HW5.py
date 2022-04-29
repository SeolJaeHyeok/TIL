import sys

input = sys.stdin.readline

n, m = map(int, input().split())
array = [int(input()) for _ in range(n)]


# 같은 숫자를 가진 마지막 폭탄의 인덱스를 구하는 함수
def get_end_index(start_idx, target):
    end_idx = start_idx  # 처음에는 시작 인덱스 = 마지막 인덱스
    for idx in range(start_idx + 1, len(array)):
        # 같은 숫자를 만나면 마지막 인덱스 증가
        if array[idx] == target:
            end_idx += 1
        # 다른 숫자를 만나면 탈출
        else:
            break
    # 마지막 인덱스 반환
    return end_idx


while True:
    flag = False  # 폭탄 터짐 여부 체크

    for cur_idx, number in enumerate(array):
        if number == 0:
            continue
        # 같은 숫자를 가진 마지막 폭탄의 인덱스 구하기
        end_idx = get_end_index(cur_idx, number)

        # 폭탄의 개수가 m개 이상일 경우
        if end_idx - cur_idx + 1 >= m:
            # 해당 범위에 있는 값을 0으로 덮어씀
            array[cur_idx:end_idx + 1] = [0] * (end_idx - cur_idx + 1)
            flag = True

    # 0으로 바뀐 값(=같은 번호를 가진 m개 이상의 연속된 폭탄)이 존재한다면 모두 삭제
    while 0 in array:
        array.remove(0)

    # 폭탄이 터지지 않으면 반복문 탈출
    if not flag:
        break

print(len(array))
for i in array:
    print(i)