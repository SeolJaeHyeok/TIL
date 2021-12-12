# 1946
# 1, 시간 초과
t = int(input())

for i in range(t):
    num = int(input())
    array = []

    for j in range(num):
        doc, meeting = map(int, input().split())
        array.append((doc, meeting))
    array.sort(key=lambda x: x[0])

    count = 0
    doc_tmp = 1e9
    meeting_tmp = 1e9
    for doc_rank, meeting_rank in array:
        if doc_rank < doc_tmp or meeting_rank < meeting_tmp:
            count += 1
            doc_tmp = doc_rank
            meeting_tmp = meeting_rank
    print(count)

# 2, 시간초과
t = int(input())

for i in range(t):
    num = int(input())
    array = []

    for j in range(num):
        doc, meeting = map(int, input().split())
        array.append((doc, meeting))

    array.sort(key=lambda x: x[0])

    count = 0
    meeting_tmp = array[0][1]
    for doc_rank, meeting_rank in array:
        if meeting_rank <= meeting_tmp:
            count += 1
            meeting_tmp = meeting_rank
    print(count)

# 3, 위와 동일한 로직이지만 입력을 받을 때 sys.stdin.readline()으로 입력받으니 시간초과 해결
import sys

t = int(input())

for i in range(t):
    num = int(input())
    array = []

    for j in range(num):
        doc, meeting = map(int, sys.stdin.readline().split())
        array.append((doc, meeting))

    array.sort()

    count = 1
    meeting_tmp = array[0][1]
    for doc_rank, meeting_rank in array:
        if meeting_rank < meeting_tmp:
            count += 1
            meeting_tmp = meeting_rank

    print(count)

"""
- 위 문제는 서류 순위를 기준으로 오름차순 정렬을 하고 면접 순위를 가지고 비교를 해서 최대 지원자수를 구하면 된다.
- 서류 순위가 1위인 사람은 무조건 선발 가능하기 떄문에 count 변수를 1로 선언하고
- 비교대상을 서류 순위가 1위인 사람의 면접 순위로 설정한다. 
- 만약 서류 순위가 1위인 사람의 면접순위가 4위라면 4를 비교대상으로 삼고 배열을 순회한다.
- 순회하면서 4보다 낮은 순위를 가진 요소를 만나면 카운팅을 해주고 비교대상을 해당 순위로 교체해준다.
- 서류 순위를 기준으로 오름차순 정렬을 했으니 비교대상인 면접 순위를 교체해주지 않으면 '적어도 하나가 다른 지원자보다 떨어지지 않는다'는 조건에 부합하지 않는다.
ex) [(1,4), (2, 5), (3, 6), (4, 2), (5, 7), (6, 1), (7, 3)]라는 서류 순위로 정렬된 리스트가 있다고 한다면
서류 순위가 1위인 지원자의 면접 순위 4를 비교대상으로 배열을 순회한다. 
만약 비교대상을 교체하지 않았을 경우의 합격한 지원자는
(1, 4), (4, 2), (6, 1), (7, 3)로 총 네 명이 된다.
이 경우 (7, 3)의 순위를 가진 지원자는 (4, 2), (6, 1)을 가진 지원자보다 두 개 모두 떨어지기 때문에 조건에 부합하지 않는다. 
하지만 비교대상을 교체해가면서 비교를 하게 되면
(1, 4), (4, 2), (6, 1)로 총 세 명이 된다. 이는 '적어도 하나가 다른 지원자보다 떨어지지 않는다'는 조건에 부합한다.
"""