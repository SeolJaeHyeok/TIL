# Reverse String
# 투 포인터를 이용한 방식 - 216ms
def reverseString(a: list):
    left, right = 0, len(a) - 1
    while left < right:
        a[left], a[right] = a[right], a[left]
        left += 1
        right -= 1
    print(a)


reverseString(["h", "e", "l", "l", "o"])

# 파이썬 라이브러리 이용 - 208ms
def reverseString(a: list):
    a.reverse()
    print(a)


reverseString(["h", "e", "l", "l", "o"])

# 리스트 슬라이싱 이용
def reverseString(a: list):
    result = a[::-1]
    print(result)


reverseString(["h", "e", "l", "l", "o"])