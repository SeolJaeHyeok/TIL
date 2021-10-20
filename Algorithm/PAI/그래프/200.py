# Number of Islands
def numIslands(grid: list) -> int:
    def dfs(i, j):
        # 더이상 땅이 아니라면 종료
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != '1':
            return

        # 방문한 곳 처리
        grid[i][j] = 0
        # 동서남북 탐색
        dfs(i + 1, j)
        dfs(i - 1, j)
        dfs(i, j + 1)
        dfs(i, j - 1)

    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                dfs(i, j)
                count += 1

    return count


print(numIslands([
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]))


"""
- 2차원 행렬의 모든 원소를 순회해서 육지(1)이라면 그 곳을 시작으로 동서남북으로 재귀호출하면서 육지를 확장해 나간다.
- 동서남북이 모두 땅이 아니라면 함수를 종료하고 카운팅을 해준다.
- dfs 함수 내에 grid[i][j]를 0으로 만들어주는 부분이 있는데 이 부분은 이미 방문한 지역을 다시 방문하는 것을 방지하기 위한 일종의 가지치기다.
이 부분을 바꾸지 않으면 if grid[i][j] == '1': 이 조건문에서 이미 탐색한 부분을 시작점으로 해서 dfs 함수를 또 다시 호출하기 때문에
이미 방문한 지역은 0으로 처리해서 재방문하지 않게 만들어 주는 것이다. 
"""