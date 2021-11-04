def solution(nums):
    answer = []
    length = len(nums) // 2
    for i in range(len(nums)):
        if len(answer) == length:
            break
        if nums[i] not in answer:
            answer.append(nums[i])

    return len(answer)