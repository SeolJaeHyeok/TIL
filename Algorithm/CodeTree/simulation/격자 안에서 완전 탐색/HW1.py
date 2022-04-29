n, m = tuple(map(int, input().split()))
board = [list(map(int, input().split())) for _ in range(n)]

# 주어진 k에 대하여 마름모의 넓이를 반환합니다.
def get_area(k):
    return k * k + (k + 1) * (k + 1)

# 주어진 k에 대하여 채굴 가능한 금의 개수를 반환합니다.
def get_num_of_gold(row, col, k):
    arr = []
    for i in range(n):
        for j in range(n):
            # (row, col)을 중심으로 상하좌우로 확장하면서 거리가 k 이하인 좌표는 마름모의 범위 안에 존재하는 것
            # 따라서 해당 좌표의 값을 추가
            if abs(row - i) + abs(col - j) <= k:
                arr.append(board[i][j])
    return sum(arr)

max_gold = 0

# 격자의 각 위치가 마름모의 중앙일 때 채굴 가능한 금의 개수를 구합니다.
for row in range(n):
    for col in range(n):
        # 만약 네 꼭지점이 중심 좌표라고 했을 경우 전체 board를 덮기 위한 k는 (n - 1) * 2
        # 따라서 k는 0부터 (n - 1) * 2까지 늘어나면서 금의 개수를 구하기
        for k in range(2 * (n - 1) + 1):
            num_of_gold = get_num_of_gold(row, col, k)

            # 손해를 보지 않으면서 채굴할 수 있는 최대 금의 개수를 저장합니다.
            if num_of_gold * m >= get_area(k):
                max_gold = max(max_gold, num_of_gold)

print(max_gold)