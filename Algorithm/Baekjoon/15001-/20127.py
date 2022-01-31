# 증가수열
def isBig():
    global N, inputs
    cnt = 0
    small = -1
    for i in range(1, N):
        if inputs[i-1] > inputs[i]:
            cnt += 1
            small = i
        if cnt > 1:
            return False
    if inputs[-1] <= inputs[0] or cnt == 0:
        return small
    else:
        return False

# 감소수열
def isSmall():
    global N, inputs
    cnt = 0
    big = -1
    for i in range(1, N):
        if inputs[i-1] < inputs[i]:
            cnt += 1
            big = i
        if cnt > 1:
            return False
    if inputs[-1] >= inputs[0] or cnt == 0:
        return big
    else:
        return False

N = int(input())
inputs = list(map(int, input().split()))

if N == 1 or len(set(inputs)) == 1:
    print(0)
    exit()

big_answer = isBig()
small_answer = isSmall()
# print(big_answer, small_answer)
if big_answer == -1 or small_answer == -1:
    print(0)
else:
    if small_answer and big_answer:
        print(min(small_answer, big_answer))
    elif small_answer and not big_answer:
        print(small_answer)
    elif big_answer and not small_answer:
        print(big_answer)
    else:
        print(-1)