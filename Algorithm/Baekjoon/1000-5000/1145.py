nums = list(map(int, input().split()))
nums.sort()

# 가장 작은 숫자부터 시작
flag = min(nums)
while True:
    count = 0
    # 다섯개의 숫자 중 나누어 떨어질 경우를 카운팅
    for i in range(5):
        if flag % nums[i] == 0:
            count += 1
    # 3회 이상 나누어 떨어질 때의 가장 작은 숫자를 출력
    if count > 2:
        print(flag)
        break
    # 3회 미만으로 나누어질 경우 검사할 숫자 증가시키기
    flag += 1
