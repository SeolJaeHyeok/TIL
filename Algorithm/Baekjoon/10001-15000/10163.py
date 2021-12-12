n = int(input())
array = [[0]*1001 for i in range(1001)]  # 빈 격자

for i in range(1, n + 1):
    x, y, w, h = map(int, input().split())
    # 입력된 색종이 크기만큼 격자에 값 채우기
    for j in range(x, x + w):
        for k in range(y, y + h):
            array[j][k] = i

# 테스트 케이스 수만큼 돌며 각 색종이 면적(격자에 존재하는 i의 개수) 출력
for i in range(1, n + 1):
    cnt = 0
    for m in array:
        cnt += m.count(i)
    print(cnt)

"""
- 입력 순서대로 일정한 값(여기서는 i)을 격자에 채워준다.
- 위의 처리를 반복하게 되면 겹치는 부분은 자동으로 가장 마지막 색종이의 값(i)으로 갱신 된다.
- 모든 처리가 끝났으면 격자에 입력된 값(i)의 개수를 세어 출력한다.
ex) 총 입력된 테스트 케이스가 3개일 경우,
격자에 입력된 1의 개수 = 첫 번째 색종이의 면적
격자에 입력된 2의 개수 = 두 번째 색종이의 면적
격자에 입력된 3의 개수 = 세 번째 색종이의 면적
"""