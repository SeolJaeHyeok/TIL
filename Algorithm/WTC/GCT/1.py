# sol
def solution(S, interval):
    S = list(S)
    for i in interval:
        s, e = i # 시작, 끝 인덱스
        # front, mid, behind로 분할
        a, b, c = S[:s-1], list(reversed(S[s-1:e])), S[e:]
        # 배열 합치기
        S = a + b + c

    return ''.join(S)


solution("abcde", [[1,3],[1,4],[4,5]])
solution("abcde", [[4,5],[1,2],[3,3]])