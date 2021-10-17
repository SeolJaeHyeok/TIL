# Palindrome Linked List
from collections import deque


# 연결리스트를 파이썬 리스트로 변환 후 풀이, 1340ms
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def isPalindrome(head: ListNode) -> bool:
    q = []
    if not head:
        return True

    node = head
    # 리스트로 변환
    while node is not None:
        q.append(node.val)
        node = node.next

    # 팰린드롬 판별
    while len(q) > 1:
        if q.pop(0) != q.pop():
            return False

    return True


# 데크를 이용한 최적화, 836ms
def isPalindrome(head: ListNode) -> bool:
    q = deque()
    if not head:
        return True

    node = head
    # 리스트로 변환
    while node is not None:
        q.append(node.val)
        node = node.next

    # 팰린드롬 판별
    while len(q) > 1:
        if q.popleft() != q.pop():
            return False

    return True


# 런너(Runner)를 이용한 풀이, 656ms
def isPalindrome(head: ListNode) -> bool:
    rev = None
    fast = slow = head
    # 런너를 이용해 역순 연결리스트 구성
    while fast and fast.next:
        fast = fast.next.next
        rev, rev.next, slow = slow, rev, slow.next

    # 입력값이 홀수개일 때의 경우 slow 런너가 중앙 값 비껴나가게 만들기
    if fast:
        slow = slow.next

    # 팰린드롬 확인
    while rev and rev.val == slow.val:
        slow, rev = slow.next, rev.next

    # 정상적으로 비교가 완료됐으면 slow와 rev 모두 끝까지 이동해 둘 다 None
    return not rev
