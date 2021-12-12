# N번째 큰 수
# 1, Heap 자료구조 구현 - 메모리 초과
class Heap:
    def __init__(self, data):
        self.heap_array = list()
        self.heap_array.append(None)
        self.heap_array.append(data)

    # 부모 노드와 자식 노드의 값을 비교해서 위쪽 방향으로 값을 바꿔줘야 하는지  확인하는 함수
    def move_up(self, inserted_idx):
        if inserted_idx <= 1:  # 루트 노드일 경우
            return False

        parent_idx = inserted_idx // 2  # 입력된 데이터의 부모 노드의 인덱스
        if self.heap_array[inserted_idx] > self.heap_array[parent_idx]:  # 입력된 데이터와 부모 노드의 데이터 비교
            return True
        else:
            return False

    # 부모 노드와 자식 노드의 값을 비교해서 아래쪽 방향으로 값을 바꿔줘야 하는지 확인하는 함수
    def move_down(self, popped_idx):
        left_child_popped_idx = popped_idx * 2
        right_child_popped_idx = popped_idx * 2 + 1

        # case1: 왼쪽 자식 노드도 없을 때
        if left_child_popped_idx >= len(self.heap_array):
            return False
        # case2: 오른쪽 자식 노드만 없을 때
        elif right_child_popped_idx >= len(self.heap_array):
            # 자식 노드의 값이 더 클 경우
            if self.heap_array[popped_idx] < self.heap_array[left_child_popped_idx]:
                return True
            else:
                return False
        # case3: 왼쪽, 오른쪽 자식 노드 모두 있을 때
        else:
            # 왼쪽 자식 노드의 값이 오른쪽 자식 노드의 값보다 크고
            if self.heap_array[left_child_popped_idx] > self.heap_array[right_child_popped_idx]:
                # 왼쪽 자식 노드의 값이 부모 노드의 값보다 클 경우 True
                if self.heap_array[popped_idx] < self.heap_array[left_child_popped_idx]:
                    return True
                else:
                    return False
            else:  # 오른쪽 자식 노드의 값이 왼쪽 자식 노드의 값보다 크고
                # 오른쪽 자식 노드의 값이 부모 노드의 값보다 클 경우 True
                if self.heap_array[popped_idx] < self.heap_array[right_child_popped_idx]:
                    return True
                else:
                    return False

    def pop(self):
        if len(self.heap_array) <= 1:
            return None

        returned_data = self.heap_array[1]
        self.heap_array[1] = self.heap_array[-1]
        del self.heap_array[-1]
        popped_idx = 1

        while self.move_down(popped_idx):
            left_child_popped_idx = popped_idx * 2
            right_child_popped_idx = popped_idx * 2 + 1

            # case2: 오른쪽 자식 노드만 없을 때
            if right_child_popped_idx >= len(self.heap_array):
                # 왼쪽 자식 노드의 값이 더 클 경우
                if self.heap_array[popped_idx] < self.heap_array[left_child_popped_idx]:
                    # SWAP
                    self.heap_array[popped_idx], self.heap_array[left_child_popped_idx] = self.heap_array[
                                                                                              left_child_popped_idx], \
                                                                                          self.heap_array[popped_idx]
                    popped_idx = left_child_popped_idx  # 부모 노드와 자식 노드 교체
            # case3: 왼쪽, 오른쪽 자식 노드 모두 있을 때
            else:
                # 왼쪽 자식 노드의 값이 오른쪽 자식 노드의 값보다 크고
                if self.heap_array[left_child_popped_idx] > self.heap_array[right_child_popped_idx]:
                    # 왼쪽 자식 노드의 값이 부모 노드의 값보다 클 경우
                    if self.heap_array[popped_idx] < self.heap_array[left_child_popped_idx]:
                        # SWAP
                        self.heap_array[popped_idx], self.heap_array[left_child_popped_idx] = self.heap_array[
                                                                                                  left_child_popped_idx], \
                                                                                              self.heap_array[
                                                                                                  popped_idx]
                        popped_idx = left_child_popped_idx  # 부모 노드와 자식 노드 교체
                # 오른쪽 자식 노드의 값이 왼쪽 자식 노드의 값보다 크고
                else:
                    # 오른쪽 자식 노드의 값이 부모 노드의 값보다 클 경우
                    if self.heap_array[popped_idx] < self.heap_array[right_child_popped_idx]:
                        # SWAP
                        self.heap_array[popped_idx], self.heap_array[right_child_popped_idx] = self.heap_array[
                                                                                                   right_child_popped_idx], \
                                                                                               self.heap_array[
                                                                                                   popped_idx]
                        popped_idx = right_child_popped_idx  # 부모 노드와 자식 노드 교체

        return returned_data

    def insert(self, data):
        if len(self.heap_array) == 0:  # 방어 코드
            self.heap_array.append(None)
            self.heap_array.append(data)
            return True

        self.heap_array.append(data)  # 일단 데이터를 배열의 맨 마지막에 추가

        inserted_idx = len(self.heap_array) - 1  # 삽입된 데이터의 인덱스를 추출

        while self.move_up(inserted_idx):  # move_up 함수를 통해 부모 노드보다 값이 크다면(move_up 함수에서 True 리턴)
            parent_idx = inserted_idx // 2  # 입력된 데이터의 부모 노드의 인덱스를 구하고
            self.heap_array[inserted_idx], self.heap_array[parent_idx] = self.heap_array[parent_idx], self.heap_array[
                inserted_idx]  # Swap
            inserted_idx = parent_idx  # 부모노드와 자식노드의 값이 바뀌었으니 해당하는 인덱스의 값도 바꿔준다.

        return True


n = int(input())
array = []
heap = Heap(-10000000000)
for i in range(n):
    array.append(list(map(int, input().split())))

for i in range(len(array)):
    for j in range(len(array)):
        heap.insert(array[i][j])

while n - 1:
    n -= 1
    heap.pop()

print(heap.pop())


# 2, 최소 힙 -> Sol
import heapq
import sys

n = int(input())
heap = []
for _ in range(n):
    nums = list(map(int, sys.stdin.readline().split()))
    if not heap:
        for num in nums:
            heapq.heappush(heap, num)
    else:
        # 힙의 원소 수를 n개로 유지
        for num in nums:
            # 새로운 수가 최소 값보다 크다면
            if num > heap[0]:
                # 새로운 수 힙에 추가하고 최소 값 추출
                heapq.heappush(heap, num)
                heapq.heappop(heap)
    # print(heap)
print(heap[0])


# 3, 최대 힙 -> 메모리 초과
n = int(input())
heap = []
for _ in range(n):
    nums = list(map(int, sys.stdin.readline().split()))

    for num in nums:
        heapq.heappush(heap, -num)


for _ in range(n - 1):
    heapq.heappop(heap)

print(-heap[0])

