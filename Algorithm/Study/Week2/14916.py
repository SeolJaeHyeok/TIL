# 거스름돈
import sys
n = int(sys.stdin.readline())

if n in [1, 3]:
    result = -1
elif (n % 5) % 2 == 0:  # 5로 나눈 나머지가 2로 나눠진다면
    # 5로 나눴을 때의 몫과 나머지를 2로 나눴을 때의 몫을 더함
    result = n // 5 + (n % 5) // 2
else:  # 5로 나눈 나머지가 2로 나눠지지 않는다면
    # 5로 나눈 몫에서 1을 빼고 나머지에 5를 더해 2로 나눈다.
    # ex) 13은 5로 나눈 나머지가 3이므로 2로 나눠지지 않는다.
    # 따라서 13을 5로 나눈 몫 2에서 1을 빼고 나머지 3에 5를 더해 8을 2로 나눴을 때의 몫을 구한 뒤 두 값을 더해준다.
    result = ((n // 5) - 1) + ((n % 5 + 5) // 2)

print(result)
