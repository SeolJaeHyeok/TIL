# 설탕 배달, 2839
n = int(input())
count = 0
while True:  # n이 0보다 크면 반복
    if n % 5 == 0:
        count += n // 5
        break
    n -= 3
    count += 1
    if n < 0:  # n이 0보다 작으면 값을 구할 수 없음
        print(-1)
        break

print(count)

"""
접근 방법
- 3과 5 중에 5로 나눌 수 있는 만큼 최대한 나누게 되면 최소 횟수를 구할 수 있음
- 5로 나눠진다면 5로 나눈 몫이 곧 최소 횟수, 5로 나눠지지 않으면 n을 업데이트 하고 다시 반복 
- n의 값이 음수가 된다면 3과 5로 구할 수 없다는 말이므로 -1 출력
"""