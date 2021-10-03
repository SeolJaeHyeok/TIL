import heapq

n = int(input())

heap = []
for _ in range(n):
    data = int(input())
    heapq.heappush(heap, data)

result = 0
while len(heap) > 1:
    one = heapq.heappop(heap)
    two = heapq.heappop(heap)
    value = one + two
    result += value
    heapq.heappush(heap, value)

print(result)

"""
접근 방법
- 문제의 핵심은 항상 가장 작은 두개의 수를 더할 경우 최적의 해를 보장한다는 것
- 따라서 최소 힙을 사용하여 가장 작은 수 두 개를 리스트에서 추출한 뒤 합을 결과에 더해주고 다시 큐에 넣어준다.
- 위 과정을 힙의 원소가 1개 남을 때까지 반복하면 된다. 
"""