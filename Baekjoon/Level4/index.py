# 10952번
while True:
    A, B = map(int, input().split())
    if A != 0 or B != 0:
        print(A + B)
    else:
        break

# 10951번
# 몇개의 테스트 케이스가 주어지는지 알 수 없기 때문에 EOF까지 입력을 받으면 된다.
try:
    while True:
        A, B = map(int, input().split())
        print(A + B)
except:
    exit()

# 1110번
# 1
num = int(input())
count = 0
result = num // 10 + num % 10  # 입력한 수의 각 자리수를 나타내는 숫자의 합
newNum = (num % 10) * 10 + result % 10  # 입력 수와 result 이용해서 새로운 수로 업이트

while True:
    # 입력한 수와 업데이트된 값이 같지 않으면
    if num != newNum:
        if newNum >= 10:
            result = newNum // 10 + newNum % 10  # 입력 수의 자리수를 가지고 result 업데이트
            newNum = (newNum % 10) * 10 + result % 10  # 새로운 result 가지고 입력 수 업데이트
            count += 1
        else:
            result = 0 + newNum % 10  # 업데이트한 입력 수가 10보다 작다면 앞 자리를 0으로 생각해서 result 업데이트
            newNum = (newNum % 10) * 10 + result % 10
            count += 1
    else:
        count += 1
        break
print(count)


# 2
def nextNumber(N):
    digitSum = 0
    n = N
    while n:
        digitSum += n % 10
        n //= 10
    return (N % 10) * 10 + digitSum % 10


def main():
    N = int(input())
    r = 1
    M = nextNumber(N)
    while M != N:
        M = nextNumber(M)
        r += 1
    print(r)

main()
