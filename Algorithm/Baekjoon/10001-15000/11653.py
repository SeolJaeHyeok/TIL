# 11653번
"""
문제
정수 N이 주어졌을 때, 소인수분해하는 프로그램을 작성하시오.

입력
첫째 줄에 정수 N (1 ≤ N ≤ 10,000,000)이 주어진다.

출력
N의 소인수분해 결과를 한 줄에 하나씩 오름차순으로 출력한다. N이 1인 경우 아무것도 출력하지 않는다.

풀이방법
1) 소인수분해는 2부터 입력한 숫자까지 나눠보는 수밖에 없다
2) 대신 나누는 수로 하여금 나눌 수 있는만큼 전부 나누고 다음 숫자로 넘어가야 한다.
"""

N = int(input())

for i in range(2, N+1):  # 2부터 시작하고 점점 증가
    if N % i == 0:  # 나누기 전에 나눌 수 있는 숫자인지 검사하기 => 속도 개선 
        while N % i == 0:  # 나눌 수 있을만큼 나누고
            N /= i
            print(i)
