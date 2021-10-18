# Merge Two Sorted Lists
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode):
        # l1와 l2 노드의 값을 앞에서부터 차례대로 비교하여 더 작은 값을 왼쪽으로 위치시키고
        if (not l1) or (l2 and (l1.val > l2.val)):
            l1, l2 = l2, l1
        # l1의 next에는 그 다음값이 엮이도록 재귀호출
        if l1:
            l1.next = self.mergeTwoLists(l1.next, l2)

        return l1