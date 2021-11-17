# 2018 카카오 블라인드 테스트 3차 
def process(num, base):
    s = '0123456789ABCDEF'
    d, m = divmod(num, base)

    if d == 0:
        return s[m]
    else:
        # q를 base로 변환
        # 즉, n진수의 다음 자리를 구함
        return process(d, base) + s[m]


def solution(n, t, m, p):
    answer = ''

    tmp = ''
    for i in range(m * t):
        tmp += str(process(i, n))

    while True:
        if len(answer) == t:
            return answer
        answer += tmp[p - 1]
        p += m