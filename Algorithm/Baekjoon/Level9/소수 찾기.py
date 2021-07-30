# 1978번
"""
문제
주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

입력
첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.

출력
주어진 수들 중 소수의 개수를 출력한다.

풀이방법
1) 소수는 1과 자기 자신을 제외하고 어떠한 수로도 나누어지지 않는 2보다 큰 자연수를 의미한다.
2) 따라서 2부터 n-1까지의 수로 나누어서 나머지가 0이면 소수가 아니기 때문에 false를 리턴 그렇지 않으면 true를 리턴
3) 함수로 만들어 입력받은 숫자를 리스트로 만든 다음 리스트 요소들을 함수의 인자로 넣어 소수여부 판별 후 counting
"""


def is_Prime(n):
    if n < 2:
        return False

    for k in range(2, n):
        if n % k == 0:
            return False

    return True


N = int(input())
nums = list(map(int, input().split()))
count = 0

for i in range(0, len(nums)):
    if is_Prime(nums[i]):
        count += 1

print(count)


