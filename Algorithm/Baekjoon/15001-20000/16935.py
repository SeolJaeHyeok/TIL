# 배열 돌리기 3, 3hour
def process(operations, array):
    for op in operations:
        if op == 1:
            # 1번 연산 - 상하 반전
            for i in range(len(array) // 2):
                array[i], array[-1-i] = array[-1-i], array[i]
        elif op == 2:
            # 2번 연산 - 좌우 반전
            for i in range(len(array)):
                array[i].reverse()
        elif op == 3:
            # 3번 연산 - 오른쪽 90도 회전
            # 먼저 상하 반전 시키고
            for i in range(len(array) // 2):
                array[i], array[-1-i] = array[-1-i], array[i]

            # 열과 행 바꿔주기
            tmp_arr = [[] for _ in range(len(array[0]))]
            for i in range(len(array[0])):
                for j in range(len(array)):
                    tmp_arr[i].append(array[j][i])

            array = tmp_arr
        elif op == 4:
            # 4번 연산 - 왼쪽으로 90도 회전
            # 먼저 좌우 반전 시키고
            for i in range(len(array)):
                array[i].reverse()

            # 열과 행 바꿔주기
            tmp_arr = [[] for _ in range(len(array[0]))]
            for i in range(len(array[0])):
                for j in range(len(array)):
                    tmp_arr[i].append(array[j][i])

            array = tmp_arr
        elif op == 5:
            # 5번 연산
            one = []
            two = []
            three = []
            four = []

            col_idx = len(array[0]) // 2

            for i in range(0, len(array) // 2):
                one.append(array[i][:col_idx])
                two.append(array[i][col_idx:])

            for i in range(len(array) // 2, len(array)):
                four.append(array[i][:col_idx])
                three.append(array[i][col_idx:])

            tmp_arr = []
            for i in range(len(one)):
                tmp_arr.append(four[i] + one[i])

            for i in range(len(three)):
                tmp_arr.append(three[i] + two[i])

            array = tmp_arr
        elif op == 6:
            # 6번 연산
            one = []
            two = []
            three = []
            four = []

            col_idx = len(array[0]) // 2

            for i in range(0, len(array) // 2):
                one.append(array[i][:col_idx])
                two.append(array[i][col_idx:])

            for i in range(len(array) // 2, len(array)):
                four.append(array[i][:col_idx])
                three.append(array[i][col_idx:])

            tmp_arr = []
            for i in range(len(one)):
                tmp_arr.append(two[i] + three[i])

            for i in range(len(three)):
                tmp_arr.append(one[i] + four[i])

            array = tmp_arr

    return array


n, m, r = map(int, input().split())
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

operations = list(map(int, input().split()))

# for i in range(len(array)):
#     for j in range(len(array[0])):
#         print(array[i][j], end=' ')
#     print()
# print()

result = process(operations, array)
for i in range(len(result)):
    for j in range(len(result[0])):
        print(result[i][j], end=' ')
    print()

