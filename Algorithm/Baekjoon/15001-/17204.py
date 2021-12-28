from collections import deque

def bfs():
    q = deque()
    q.append(0)
    count = 0
    # 게임에 참여한 사람 수만큼 반복
    for _ in range(n):
        # 영기(0)부터 시작
        target = q.popleft()
        count += 1 # 지목 횟수 카운팅

        # 보성이의 번호를 지목했으면 여태껏 지목한 횟수 반환
        if array[target] == k:
            return count

        # 지목한 번호 다시 추가
        q.append(array[target])

    # 모든 사람 수만큼 반복후에도 보성이 번호를 지목하지 않았으면 -1 리턴
    return -1


n, k = map(int, input().split())
array = [int(input()) for _ in range(n)]

print(bfs())


