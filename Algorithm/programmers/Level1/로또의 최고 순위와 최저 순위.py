def solution(lottos, win_nums):
    table = {
        0: 6,
        1: 6,
        2: 5,
        3: 4,
        4: 3,
        5: 2,
        6: 1
    }
    answer = []
    count = 0
    for i in range(len(lottos)):
        if lottos[i] in win_nums:
            count += 1

    max_grade = table[count + lottos.count(0)]
    min_grade = table[count]

    return [max_grade, min_grade]