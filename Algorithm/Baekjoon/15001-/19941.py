# 햄버거 분배
n, k = map(int, input().split())
data = list(input())

count = 0
for i in range(len(data)):
    # 사람인 경우
    if data[i] == 'P':
        # 양 쪽으로 거리가 k 이하인 범위를 왼쪽부터 탐색
        for j in range(i-k, i+k+1):
            # 사람을 기준으로 가능한 왼쪽부터 오른쪽으로 탐색하여 채우기
            if 0 <= j < n and data[j] == 'H':
                data[j] = 'E' # 햄버거 먹고 방문 처리
                count += 1
                break
print(count)

"""
거리가 k 이하인 범위 내에서 햄버거를 먹을 수 있다고 했는데 최대한 많은 사람이 햄버거를 먹으려면 가능한 왼쪽부터 채워야 된다.
따라서 가능한 범위의 왼쪽 끝부터 오른쪽 끝으로 탐색해가면서 햄버거가 있으면 방문 처리한다.  
"""

