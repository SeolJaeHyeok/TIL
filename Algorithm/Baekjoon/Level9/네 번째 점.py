# 3009 번
"""
문제
세 점이 주어졌을 때, 축에 평행한 직사각형을 만들기 위해서 필요한 네 번째 점을 찾는 프로그램을 작성하시오.

입력
세 점의 좌표가 한 줄에 하나씩 주어진다. 좌표는 1보다 크거나 같고, 1000보다 작거나 같은 정수이다.

출력
직사각형의 네 번째 점의 좌표를 출력한다.

풀이방법
1) 축에 평행인 직사각형을 구하려면 x좌표, y좌표가 각각 두 개씩 있어야 한다.
2) 세개 점의 x, y 값을 리스트로 만든 다음 리스트 요소들을 count하여 1개인 요소(네 번째 점)를 찾아 해당 값을 target에 저장하고 출력
"""

x_list = []
y_list = []

for _ in range(3):
    x, y = map(int, input().split())
    x_list.append(x)
    y_list.append(y)

x_target = y_target = 0
for i in range(3):
    if x_list.count(x_list[i]) == 1:
        x_target = x_list[i]
    if y_list.count(y_list[i]) == 1:
        y_target = y_list[i]

print(x_target, y_target)