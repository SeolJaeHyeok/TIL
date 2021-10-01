# 럭키 스트레이트
n = input()
center = len(n) // 2
a = n[:center]
b = n[center:]

sum1 = 0
sum2 = 0
for x, y in zip(a, b):
    sum1 += int(x)
    sum2 += int(y)

# print(sum1, sum2)
if sum1 == sum2:
    print('LUCKY')
else:
    print('READY')


# sol
n = input()
length = len(n) # 점수 값의 총 자릿수
summary = 0

# 왼쪽 부분의 자릿수의 합 더하기
for i in range(length // 2):
    summary += int(n[i])

# 오른쪽 부분의 자릿수의 합 빼기
for i in range(length // 2, length):
    summary -= int(n[i])

# 왼쪽 부분과 오른쪽 부분의 자릿수 합이 동일한지 검사
if summary == 0:
    print("LUCKY")
else:
    print("READY")


"""
접근 방법
- 입력값은 항상 짝수로 들어온다고 했으니 입력된 문자열의 길이를 반으로 나눠 각 자리수를 더해주고 비교하는 형태로 구현
- solution은 왼쪽 값을 더하고 오른쪽 값을 빼서 0이면 두 개의 값이 같다는 로직으로 구현
"""