# Trapping Rain Water
# 투 포인터 이용 방식, , 99ms
def trap(height: list):
    if not height:
        return 0

    volume = 0
    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]

    while left < right:
        # 최대 높이의 기둥 갱신
        left_max, right_max = max(height[left], left_max), max(height[right], right_max)

        # 더 높은 쪽을 향해 투 포인터 이동
        # 오른쪽 기둥의 최대 높이가 왼쪽 기둥의 최대 높이보다 크거나 같은 경우 왼쪽 인덱스 이동
        if left_max <= right_max:
            # 최대 높이의 기둥과 현재 높이와의 차이만큼 더한 다음(0인 경우도 존재)
            volume += left_max - height[left]
            # 오른쪽으로 한 칸 이동
            left += 1
        # 왼쪽 기둥의 최대 높이가 오른쪽 기둥의 최대 높이보다 큰 경우 오른쪽 인덱스 이동
        else:
            # 최대 높이의 기둥과 현재 높이와의 차이만큼 더한 다음(0인 경우도 존재)
            volume += right_max - height[right]
            # 왼쪽으로 한 칸 이동
            right -= 1

    return volume


result = trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
print(result)


# 스택을 쌓아서 구현하는 방식, 이해x
def trap(height: list):
    stack = []
    volume = 0

    for i in range(len(height)):
        while stack and height[i] > height[stack[-1]]:
            # 스택에서 꺼낸다
            top = stack.pop()

            if not len(stack):
                break

            # 이전과의 차이만큼 물 높이 처리
            distance = i - stack[-1] - 1
            waters = min(height[i], height[stack[-1]]) - height[top]

            volume += distance * waters

        stack.append(i)

    return volume


result = trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
print(result)
