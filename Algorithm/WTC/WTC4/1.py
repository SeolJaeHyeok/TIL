def solution(arr):
    one = arr.count(1)
    two = arr.count(2)
    three = arr.count(3)
    max_count = max(one, two, three)

    return [max_count - one, max_count - two, max_count - three]