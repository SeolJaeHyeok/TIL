import sys
input = sys.stdin.readline

n = int(input())

answer = []
count = 0


def beautiful_nums():
    global count
    if len(answer) == n:
        start_idx = 0  # 탐색을 시작할 인덱스
        flag = True
        while start_idx < n:
            # 배열의 요소가 연속하여 해당 요소의 값만큼 나올 수 없는 경우 아름다운 수 X
            # Ex) n = 1일 경우,
            # [4] => start_idx(0) + answer[start_idx](4)는 n보다 크므로 아름다운 수가 될 수 없다.
            if start_idx + answer[start_idx] > n:
                flag = False
                break

            # 아름다운 수가 될 수 있는 경우 start_idx부터 연속하여 해당 숫자만큼의 수가 있는지 확인
            for i in range(start_idx, start_idx + answer[start_idx]):
                # 만약 다른 숫자가 있는 경우 탈출
                if answer[start_idx] != answer[i]:
                    flag = False
                    break

            # 시작 인덱스 해당 요소의 값만큼 늘려주기
            start_idx += answer[start_idx]

        if flag:
            count += 1

        return

    for i in range(1, 5):
        answer.append(i)
        beautiful_nums()
        answer.pop()


beautiful_nums()
print(count)