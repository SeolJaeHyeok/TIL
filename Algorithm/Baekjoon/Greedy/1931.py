# 1931
# 1, 시간 초과 - 반복문으로 시작시간을 변화하면서 모든 경우를 탐색했기 때문에
# n = int(input())
# time_table = []
#
# for _ in range(n):
#     start, end = map(int, input().split())
#     time_table.append((start, end))
#
# count = 0
# result = []
# for i in range(len(time_table)):
#     start, end = time_table[i]
#     count += 1
#     for j in range(len(time_table)):
#         if time_table[j][0] >= end:
#             end = time_table[j][1]
#             count += 1
#     result.append(count)
#     count = 0
#
# print(max(result))


# 2, 시간 초과 - 위와 동일
n = int(input())
time_table = []

for _ in range(n):
    start, end = map(int, input().split())
    time_table.append((start, end))

time_table.sort()

count = 0
result = []
for i in range(len(time_table)):
    start, end = time_table[i]
    count += 1
    for j in range(i, len(time_table)):
        if time_table[j][0] >= end:
            end = time_table[j][1]
            count += 1
    result.append(count)
    count = 0

print(max(result))

# 3, sol
n = int(input())
time_table = []

for _ in range(n):
    time_table.append(tuple(map(int, input().split())))

time_table.sort(key=lambda x: (x[1], x[0]))  # 끝나는 시간과 시작 시간을 기준으로 정렬

finish = 0  # 끝나는 시간을 갱신할 변수
count = 0
# 정렬된 테이블을 순회하면서
for start, end in time_table:
    # 시작시간이 끝나는 시간보다 크거나 같다면
    if start >= finish:
        finish = end  # 끝나는 시간 갱신
        count += 1

print(count)


"""
- 이 문제의 핵심은 시작시간이 이전 회의의 종료시간보다 같거나 커야한다는 것이다.
- 그러기 위해서는 입력된 데이터를 끝나는 시간을 기준으로 정렬해야 한다. 
- 그다음으로 이전 회의의 종료시간과 시작시간을 비교하여 카운팅하면 되는데 한가지 고려해야할 문제는 끝나는 시간과 시작시간이 같을 수도 있다는 것이다.
- 그렇기 때문에 끝나는 시간을 기준으로 정렬된 데이터를 다시 시작 시간을 기준으로 정렬해주어야 한다.
- 그 후에 정렬된 데이터를 순회하며 시작시간과 종료시간을 비교하면서 카운팅하면 된다.
ex) 
5
0 8
1 3
3 5
7 8
6 7

위와 같은 데이터가 입력됐다고 하면 종료시간을 기준으로 정렬을 하지 않은 상태에서는 (0, 8) 한 번의 회의가 가능하지만 끝나는 시간으로 정렬을 하면
(1, 3), (3, 5), (6, 7), (7, 8)과 같이 회의가 가능하다.
또한 끝나는 시간이 같다면 빨리 시작되는 순서로 정렬이 되어야 한다.
예를 들어
3
3 3
1 3
2 3
와 같이 데이터가 입력됐다고 할 때, 시작시간으로 정렬이 되지 않으면 (3, 3) 한 번의 회의만 가능하지만 정렬이 된다면 (1, 3), (3, 3) 두 번의 회의가 가능하다.

이처럼 입력된 데이터를 끝나는 시간으로 정렬을 하고 난 다음 시작 시간으로 정렬을 하면 최적의 해를 구할 수 있는 테이블이 마련된다.  
"""