from collections import defaultdict

def solution(participant, completion):
    answer = ''
    data = defaultdict(int)
    for p in participant:
        data[p] += 1

    for c in completion:
        if data[c]:
            data[c] -= 1

    for key in data.keys():
        if data[key] == 1:
            answer = key

    return answer


from collections import Counter

def solution(participant, completion):
    answer = list((Counter(participant) - Counter(completion)).keys())
    return answer[0]

