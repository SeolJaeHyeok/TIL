def solution(n):
    tmp = ''
    while n:
        tmp += str(n % 3)
        n = n // 3

    answer = int(tmp, 3)
    return answer


# ..?
import string

tmp = string.digits+string.ascii_lowercase
def convert(num, base) :
    q, r = divmod(num, base)
    if q == 0 :
        return tmp[r]
    else :
        return convert(q, base) + tmp[r]

def solution(n):
    return int(convert(n, 3)[::-1], 3)