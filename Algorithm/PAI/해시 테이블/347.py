# Top K Frequent Elements
# Counter 모듈 이용, 140ms
from collections import Counter

def topKFrequent(nums: list, k: int):
    freq = Counter(nums)
    return [i for i, _ in freq.most_common(k)]


print(topKFrequent([1, 1, 1, 2, 2, 3], 2))
print(topKFrequent([1, 1, 1, 2, 2, 3], 1))
print(topKFrequent([1, 1, 1, 2, 2, 3], 3))
print(topKFrequent([1, 2], 2))


# Counter와 heapq 모듈 이용, 147ms
import heapq

def topKFrequent(nums: list, k: int):
    freqs = Counter(nums)
    heap = []

    # 최소힙이 아닌 최대힙으로 사용하기 위해 빈도수를 음수로 삽입
    for f in freqs:
        # 빈도 수(배열 안에 있는 수의 빈도)를 키로 하고 freqs의 키(배열 안에 있는 수)를 값으로 힙에 저장. 즉 키/값을 바꿔서 힙에 추가
        # 힙은 키 순서대로 정렬이 되기 때문에 빈도 수를 키로 하여 추가
        # 이렇게 음수로 추가하면 빈도수가 가장 높은 수가 가장 작은 음수가 되기 때문에 최소 힙으로 최대 힙의 효과를 얻을 수 있다.
        heapq.heappush(heap, (-freqs[f], f))

    result = []

    # k번 만큼 추출, 최소 힙이므로 가장 작은 음수 순으로 추출
    for _ in range(k):
        # heapq.heappop(heap)[1]은 freqs의 키(배열 안에 있는 수)
        result.append(heapq.heappop(heap)[1])

    return result


print(topKFrequent([1, 1, 1, 2, 2, 3], 2))
print(topKFrequent([1, 1, 1, 2, 2, 3], 1))
print(topKFrequent([1, 1, 1, 2, 2, 3], 3))
print(topKFrequent([1, 2], 2))


# Pythonic Way, 180ms
def topKFrequent(nums: list, k: int):
    return list(zip(*Counter(nums).most_common(k)))[0]

print(topKFrequent([1, 1, 1, 2, 2, 3], 2))
print(topKFrequent([1, 1, 1, 2, 2, 3], 1))
print(topKFrequent([1, 1, 1, 2, 2, 3], 3))
print(topKFrequent([1, 2], 2))
