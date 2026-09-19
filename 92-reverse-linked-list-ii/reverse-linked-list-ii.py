# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:
        dummy = ListNode(0, head)

        leftPrev, cur = dummy, head

        # iterate till left
        for i in range(left - 1):
            leftPrev, cur = cur, cur.next

        # reverse from left to right
        prev = None
        for i in range(right - left + 1):
            tempNext = cur.next
            cur.next = prev
            prev, cur = cur, tempNext

        # prev node is at right node
        # cur will be one node after right
        leftPrev.next.next = cur
        leftPrev.next = prev

        return dummy.next