# 1193번
"""
문제
무한히 큰 배열에 다음과 같이 분수들이 적혀있다.

1/1	1/2	1/3	1/4	1/5	…
2/1	2/2	2/3	2/4	…	…
3/1	3/2	3/3	…	…	…
4/1	4/2	…	…	…	…
5/1	…	…	…	…	…
…	…	…	…	…	…ㅇ

이와 같이 나열된 분수들을 1/1 -> 1/2 -> 2/1 -> 3/1 -> 2/2 -> … 과 같은 지그재그 순서로 차례대로 1번, 2번, 3번, 4번, 5번, … 분수라고 하자.
X가 주어졌을 때, X번째 분수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 X(1 ≤ X ≤ 10,000,000)가 주어진다.

출력
첫째 줄에 분수를 출력한다.

풀이방법
사선 라인이 짝수번째인지 홀수번째인지에 따라 입력받는 수에 대응하는 분수를 찾는 규칙이 달라지는 점을 이용
"""

# 1
input_num = int(input())

line = 0  # 사선 라인
max_num = 0  # 입력된 숫자(input_num 변수)의 라인에서 가장 큰 숫자
while input_num > max_num:
    line += 1
    max_num += line

gap = max_num - input_num
if line % 2 == 0:  # 사선 라인이 짝수번째 일 때
    top = line - gap  # 분자
    under = gap + 1  # 분모
else:  # 사선 라인이 홀수번째 일 때
    top = gap + 1  # 분자
    under = line - gap  # 분모

print(f'{top}/{under}')

# 2
import math

k = int(input())
x = math.ceil((-1 + math.sqrt(1+8*k))/2)
y = k - x*(x-1)/2

if x % 2 == 1:
    print(str(int(x-y+1))+"/"+str(int(y)))
else:
    print(str(int(y))+"/"+str(int(x-y+1)))

