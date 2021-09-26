# 무지의 먹방 라이브
# 16.1/100
def solution(food_times, k):
    answer = 0

    for i in range(1, k + 1):
        if sum(food_times) <= k:
            return -1
        if k < len(food_times):
            answer = i + 1
        else:
            answer = (k % len(food_times)) + 1

    return answer


# sol
import heapq

def solution(food_times, k):
    # 전체 음식을 먹는 시간보다 k가 크거나 같다면 -1
    if sum(food_times) <= k:
        return -1

    # 시간이 작은 음식부터 빼야 하므로 우선순위 큐를 이용
    q = []
    for i in range(len(food_times)):
        # (음식 시간, 음식 번호) 형태로 우선순위 큐에 삽입
        heapq.heappush(q, (food_times[i], i + 1))

    sum_value = 0 # 먹기 위해 사용한 시간
    previous = 0 # 직전에 다 먹은 음식 시간
    length = len(food_times) # 남은 음식의 개수

    # sum_value + (현재의 음식 시간 - 이전 음식 시간) * 현재 음식 개수와 k 비교
    while sum_value + ((q[0][0] - previous) * length) <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now - previous) * length
        length -= 1 # 다 먹은 음식 제외
        previous = now # 이전 음식 시간 재설정

    # 남은 음식 중에서 몇 번째 음식인지 확인하여 출력
    result = sorted(q, key=lambda x: x[1]) # 음식의 번호 기준으로 정렬
    return result[(k - sum_value) % length][1]


"""
단순 그리디 문제인줄 알았는데 우선 순위 큐를 이용하여 해결한다는 것을 생각지도 못했따..
접근 방법
- 우선 순위 큐를 이용해서 남은 시간이 적은 음식부터 확인하면서 
- 음식의 수를 최대한 줄인 뒤에는 K시간 이후에 어떤 음식을 먹으면 되는지 확인
"""