# Reverse Linked List
# 반복 구조로 구현(1) , 72ms
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode):
        node, prev = head, None

        while node:
            next, node.next = node.next, prev
            prev, node = node, next

        return prev

# 반복 구조로 구현(2) - 가장 나한테 이해가 잘되는 방법, 43ms
class Solution:
    def reverseList(self, head: ListNode):
        prev = None

        # head를 한 칸씩 움직이면서 이전 노드들까지의 역순 연결리스트 만들기
        while head:
            temp = head
            head = head.next
            temp.next = prev
            prev = temp

        return prev

# 재귀 구조로 구현, 59ms
class Solution:
    def reverseList(self, head: ListNode):
        def reverse(node: ListNode, prev: ListNode = None):
            if not node:
                return prev
            next, node.next = node.next, prev
            return reverse(next, node)

        return reverse(head)