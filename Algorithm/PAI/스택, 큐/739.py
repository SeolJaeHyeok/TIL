# Daily Temperatures
# 스택을 사용한 구현
def dailyTemperatures(temperatures: list):
    # 결과를 저장할 리스트 초기화
    result = [0] * len(temperatures)
    stack = []

    for i, cur in enumerate(temperatures):
        # 스택이 존재하고 현재 온도가 스택에 쌓인 마지막 인덱스에 해당하는 온도보다 높다면
        while stack and cur > temperatures[stack[-1]]:
            # 스택의 마지막 인덱스 꺼내고
            last = stack.pop()
            # 결과값에 현재 인덱스와 마지막 인덱스의 차이만큼 저장
            result[last] = i - last
        # 스택에 인덱스 추가
        stack.append(i)
        # print(stack)

    return result


print(dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))