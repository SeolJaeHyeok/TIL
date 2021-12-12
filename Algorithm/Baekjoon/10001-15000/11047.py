# 11047
# 1
n, k = map(int, input().split())

array = [0] * n
for i in range(n):
    num = int(input())
    array[n - 1 - i] = num

count = 0
for coin in array:
    if k == 0:
        break
    if coin > k:
        continue
    count += k // coin
    k %= coin

print(count)

"""
- 오름차순으로 입력이 된다고 명시되었으므로 큰 단위부터 확인하기 위해 내림차순으로 정렬하는 sort 메서드를 이용하는 것보다
- 오름차순 입력을 받을 때 내림차순으로 배열에 저장되면 좋겠다는 생각에 n만큼의 빈 배열을 미리 확보하고
- 마지막 인덱스부터 0번째 인덱스까지의 순서로 배열에 저장
ex) n = 10이고 동전의 단위가 1, 5, 10, 50 ... 50000일 때, 길이가 n인 빈 배열을 선언해준다. ex) array = [0] * n
원래대로라면 0번 인덱스부터 n-1번째 인덱스까지 차례대로 입력이 될 것인데 이를 n-1 인덱스부터 0번 인덱스까지 순서대로 입력이 되도록 만들어 준다.
그렇게 되면 오름차순으로 입력되는 값들은 끝에서부터 0번째 인덱스까지 차례대로 입력이 되고 이는 내림차순으로 정렬한 것과 동일한 효과가 있다.
- 사실 왜 갑자기 이런 짓을 한지 이해 안감 나도
"""

# 2, 정렬 라이브러리 사용
n, k = map(int, input().split())

array = []
for i in range(n):
    array.append(int(input()))

array.sort(reverse=True)

count = 0
for coin in array:
    if k == 0:
        break
    if coin > k:
        continue
    count += k // coin
    k %= coin

print(count)


# 3, range함수 이용
n, k = map(int, input().split())

array = []
for _ in range(n):
    array.append(int(input()))

count = 0

for i in range(n-1, -1, -1):
    if k == 0:
        break
    if array[i] > k:
        continue
    count += k // array[i]
    k %= array[i]

print(count)