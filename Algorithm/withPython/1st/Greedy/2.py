# 곱하기 혹은 더하기
# solve
str = input()

result = int(str[0])
for i in range(1, len(str)):
    num = int(str[i])
    if result != 0:
        if num <= 1:
            result += int(num)
        else:
            result *= int(num)
    else:
        result = int(num)

print(result)


# sol
data = input()

# 첫 번째 문자를 숫자로 변경하여 대입
result = int(data[0])

for i in range(1, len(data)):
    # 두 수 중에서 하나라도 '0' 혹은 '1'인 경우, 곱하기보다는 더하기 수행
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)

"""
접근 방법
- 핵심 아이디어 -> 두 수에 대하여 연산을 할 때, 두 수 중에서 하나라도 0 또는 1이라면 더하기 연산을 하고 아니라면 곱하기 연산
"""