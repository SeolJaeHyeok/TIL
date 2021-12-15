# k번째 소수
BIG_NUM = 10**7

k = int(input())
array = [1 for _ in range(BIG_NUM + 1)]

answer = []
for i in range(2, BIG_NUM + 1):
    # i가 소수라면
    if array[i]:
        answer.append(i)
        # i의 배수는 소수가 아닌 수
        for j in range(i+i, BIG_NUM + 1, i):
            array[j] = 0

print(answer[k - 1])
