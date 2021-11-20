def solution(n, words):
    answer = [0, 0]
    # 첫 단어는 항상 올바르기 때문에 count = 1
    count = 1
    # 마찬가지로 두 번째 단어부터 순환
    for i in range(1, len(words)):
        # 차례 계산
        count %= n
        # 현재 단어
        word = words[i]

        # 현재 단어의 시작이 이전 단어의 마지막과 다르거나
        # 현재 단어가 이전에 이미 나왔던 단어일 경우
        if (word[0] != words[i - 1][-1]) or (word in words[0:i]):
            return [count + 1, 1 + i // n]

        count += 1

    return answer
