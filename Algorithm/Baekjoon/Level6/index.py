# 15596번
def solve(a):
    return sum(a)

result = solve([1,2,3,4,5,6,7,8,9,10])
print(result)

# 4673번 - 셀프 넘버
"""
셀프 넘버는 1949년 인도 수학자 D.R. Kaprekar가 이름 붙였다. 양의 정수 n에 대해서 d(n)을 n과 n의 각 자리수를 더하는 함수라고 정의하자. 예를 들어, d(75) = 75+7+5 = 87이다.
양의 정수 n이 주어졌을 때, 이 수를 시작해서 n, d(n), d(d(n)), d(d(d(n))), ...과 같은 무한 수열을 만들 수 있다.
예를 들어, 33으로 시작한다면 다음 수는 33 + 3 + 3 = 39이고, 그 다음 수는 39 + 3 + 9 = 51, 다음 수는 51 + 5 + 1 = 57이다. 이런식으로 다음과 같은 수열을 만들 수 있다.
33, 39, 51, 57, 69, 84, 96, 111, 114, 120, 123, 129, 141, ...
n을 d(n)의 생성자라고 한다. 위의 수열에서 33은 39의 생성자이고, 39는 51의 생성자, 51은 57의 생성자이다.
생성자가 한 개보다 많은 경우도 있다. 예를 들어, 101은 생성자가 2개(91과 100) 있다.
생성자가 없는 숫자를 셀프 넘버라고 한다. 100보다 작은 셀프 넘버는 총 13개가 있다. 1, 3, 5, 7, 9, 20, 31, 42, 53, 64, 75, 86, 97
10000보다 작거나 같은 셀프 넘버를 한 줄에 하나씩 출력하는 프로그램을 작성
"""
# 1
# n과 n의 각 자리수를 더하는 함수 = 생성자 만드는 함수
def d(n):
    n += sum(map(int, str(n)))  # n=1994, 1994 + 23(=sum([1+9+9+4]))
    return n  # 생성자 리턴


natural_num = set(range(1, 10001))  # 중복 제거를 위해 집합자료형으로 선언
generated_num = set()  # 생성자가 있는 집합을 추가할 빈 집합
self_num = []  # 셀프 넘버를 저장할 빈 리스트
for i in range(len(natural_num)):  # 1~10000까지 돌면서
    generated_num.add(d(i))  # 중복 없애면서 생성자 추가

self_num = sorted(natural_num - generated_num)  # 전체 자연수에서 생성자가 있는 수 뺸 다음 정렬

for selfNum in self_num:
    print(selfNum)  # 생성자가 없는 수(셀프 넘버) 출력

# 2
natural_num = set(range(1,10001))  # 1~10000까지 자연수 집합자료형으로 선언
generated_num = set()

for i in range(1, 10001):  # i = 1994
    for j in str(i):  # "1", "9", "9", "4"
        i += int(j)  # 1994+1+9+9+4
    generated_num.add(i)  # 생성자가 있는 숫자들, 집합 자료형이므로 중복된 숫자 제거

self_num = sorted(natural_num - generated_num)  # 1~10000까지의 모든 자연수에서 생성자가 있는 숫자를 뺴면 self number
for selfNum in self_num:
    print(selfNum)

# 1065번 - 한수
"""
어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다.
등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다.
N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성
"""
# 이전 코드
def Hansoo(n):
    count = 0
    for i in range(1, n+1):
        numStr = str(i)
        if 1 <= i < 100:
            count += 1
        elif 100 <= i < 1000:
            if (int(numStr[0]) - int(numStr[1])) == (int(numStr[1]) - int(numStr[2])):
                count += 1
            else:
                continue
        else:
            print('1부터 1000까지의 숫자만 입력해주세요')
    return count

# 개선 후 코드
def Hansoo(n):
    count = 0
    for i in range(1, n+1):
        if 1 <= i < 100:
            count += 1
        elif 100 <= i <= 1000:
            numStr = list(map(int, str(i)))
            if numStr[0] - numStr[1] == numStr[1] - numStr[2]:
                count += 1
            else:
                continue
    return count


N = int(input())
result = Hansoo(N)
print(result)





