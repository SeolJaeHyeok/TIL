# 1
n, l = map(int, input().split())

loc = list(map(int, input().split()))
loc.sort()

# 테이프가 물을 막을 수 있는 범위
start = loc[0]
end = loc[0] + l
count = 1
for i in range(len(loc)):
    # 물이 새는 위치가 테이프가 막을 수 있는 범위 안에 있다면 무시
    if start <= loc[i] < end:
        continue
    # 범위가 벗어난다면 범위 갱신 후 카운팅
    start = loc[i]
    end = loc[i] + l
    count += 1

print(count)

# 2
n, l = map(int, input().split())
loc = list(map(int, input().split()))

# 전체 범위에 대한 리스트
coord = [False] * 1001
# 구멍이 났으면 True
for i in loc:
    coord[i] = True

ans = 0
x = 0 # 시작점을 기준으로 오른쪽으로 움직일 좌표 변수
while x < 1001:
    # 구멍이 난 경우
    if coord[x]:
        # 테이프의 길이만큼 좌표 이동
        x += l
        ans += 1
    else:
        x += 1

print(ans)


