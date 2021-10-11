# Valid Palindrome
# 리스트로 변환하여 구현한 방법 - 304ms
def isPalindrome(s):
    array = []
    for char in s:
        if char.isalnum():
            array.append(char.lower())

    while len(array) > 1:
        if array.pop(0) != array.pop():
            return False

    return True


s = input()

if isPalindrome(s):
    print('true')
else:
    print('false')


# 데크 자료형을 이용한 방법 - 64ms, popleft() 메서드가 O(1)의 시간복잡도를 가지고 있고 pop(n) 메서드는 O(n)의 시간복잡도를 가지고 있어서 훨씬 빠르다.
from collections import deque

def isPalindrome(s:str):
    array = deque()
    for char in s:
        if char.isalnum():
            array.append(char.lower())

    while len(array) > 1:
        if array.popleft() != array.pop():
            return False

    return True


s = input()

if isPalindrome(s):
    print('true')
else:
    print('false')


# "A man, a plan, a canal: Panama"
