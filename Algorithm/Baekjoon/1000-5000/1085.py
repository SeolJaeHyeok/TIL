# 1085번
"""
문제
한수는 지금 (x, y)에 있다. 직사각형은 각 변이 좌표축에 평행하고, 왼쪽 아래 꼭짓점은 (0, 0), 오른쪽 위 꼭짓점은 (w, h)에 있다.
직사각형의 경계선까지 가는 거리의 최솟값을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 x, y, w, h가 주어진다.

출력
첫째 줄에 문제의 정답을 출력한다.

풀이방법
1) 직사각형 안에서 가장 가까운 거리를 찾을 때는 대각선은 고려할 필요가 없다.
2) 따라서 직사각형 내의 한 점에서 상하좌우로 이동할 수 있는 경우는 x, y, w-x, h-y 총 네 가지 경우가 있다.
3) 이 중 최솟값을 구하면 되므로 min()을 이용하여 구해준다.
"""

# 1
x, y, w, h = map(int, input().split())
print(min(x, y, w-x, h-y))

# 2
x, y, w, h = map(int, input().split())

target = 0

if w - x >= h - y:
    target = h - y
    if target > x and x < y:
        target = x
    elif target > y and x > y:
        target = y
else:
    target = w - x
    if target > x and x < y:
        target = x
    elif target > y and x > y:
        target = y

print(target)


