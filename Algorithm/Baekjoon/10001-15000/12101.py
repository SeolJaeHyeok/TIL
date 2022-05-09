import sys
input = sys.stdin.readline

n, k = map(int, input().split())

def Choose(sum_value, ans):
    global k
    if sum_value > n:
        return

    if sum_value == n:
        k -= 1
        if k == 0:
            print(ans[:-1])
            sys.exit()

    for i in range(1, 4):
        answer.append(i)
        Choose(sum_value + i, ans + str(i) + '+')
        answer.pop()

answer = []
Choose(0, '')
print(-1)