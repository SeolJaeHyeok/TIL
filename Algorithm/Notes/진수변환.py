# 10진법을 n진법으로 바꾸기, 반복문 이용
def solution(n, q):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)

    return rev_base[::-1]
    # 역순인 진수를 뒤집어 줘야 원래 변환 하고자하는 base가 출력


print(solution(45, 2))
print(solution(45, 3))
print(solution(45, 8))
print(solution(45, 10))
print(solution(45, 12))
print(solution(45, 16))
print()

# 2018 카카오 블라인드 3차 n진수 변환, 재귀 이용
# 진수 변환
import string

def convert(num, base):
    tmp = string.digits + string.ascii_lowercase
    q, r = divmod(num, base)
    if q == 0:
        return tmp[r]
    else:
        return convert(q, base) + tmp[r]


print(convert(45, 2))
print(convert(45, 3))
print(convert(45, 8))
print(convert(45, 10))
print(convert(45, 12))
print(convert(45, 16))
