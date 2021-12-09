n = int(input())

array = []
for _ in range(n):
    array.append(int(input()))

array.sort(reverse=True)

answer = 0
count = 1
for i in range(len(array)):
    if count < 3:
        answer += array[i]
    else:
        count = 0

    count += 1

print(answer)


import sys

input = sys.stdin.readline
n = int(input())
price = []
for i in range(n):
    price.append(int(input()))

# 무료로 받는 제품의 값이 클수록 최소 가격으로 구매 가능 따라서 내림차순으로 정렬
price.sort(reverse=True)

answer = 0
for i in range(n):
    # (2+1)에서 1에 해당하는 경우 더하지 않는다.
    if i % 3 == 2:
        continue
    else:
        answer += price[i]

print(answer)

'''
아이디어
1) 내림차순 정렬
2) 2+1의 1에 해당되는 것의 금액이 비쌀수록 좋다.
3) (3의배수-1) 인덱스에 위치한 것(무료 제품)을 제외한 나머지의 요소 합을 구한다.
'''