# 안테나
n = int(input())
array = list(map(int, input().split()))
result = []

for i in range(len(array)):
    total = 0
    for j in range(len(array)):
        total += abs(array[i] - array[j])
    result.append(total)


index = result.index(min(result))
print(array[index])

# sol
n = int(input())
array = list(map(int, input().split()))
array.sort()

print(array[(n - 1) // 2])


"""
핵심 아이디어
- 중간값에 해당하는 위치의 집에 안테나를 설치했을 때, 모든 집까지의 거리의 합이 최소가 된다.
접근 방법
- 각 집마다 모든 집들 사이의 거리를 합한 결과를 구하여 리스트에 추가하고
- 해당 리스트의 최솟값의 인덱스를 구한 뒤 출력
"""