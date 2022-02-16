import sys
input = sys.stdin.readline

def hanoi(n, start, via, destination):
    """
    :param n: 원판의 개수
    :param start: 시작 기둥
    :param via: 보조 기둥(이동 시 이용하는 기둥)
    :param destination: 목적지 기둥
    """
    if n <= 1:
        # 원판이 1개 남았으면
        print(start, destination)
    else:
        # 1번 기둥의 n-1개의 원판을 2번 기둥으로 옮김
        hanoi(n - 1, start, destination, via)
        # 1번 기둥의 가장 큰 원판을 3번 기둥으로 옮김
        hanoi(1, start, via, destination)
        # 2번 기둥의 원판을 3번 기둥으로 옮김
        hanoi(n - 1, via, start, destination)


n = int(input())
print(2**n - 1) # 원판이 n개 있으면 이동 횟수는 항상 2^n - 1번
if n <= 20:
    hanoi(n, 1, 2, 3)
