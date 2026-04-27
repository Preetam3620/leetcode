# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = 0
        counter = 0
        while l1 != None:
            num1 += (l1.val * 10**counter)
            l1 = l1.next
            counter += 1

        num2 = 0
        counter = 0
        while l2 != None:
            num2 += (l2.val * 10**counter)
            l2 = l2.next
            counter += 1

        res = num1 + num2

        head = ListNode(0)
        current = head

        if res == 0:
            current.next = ListNode(0)
        else:
            while res > 0:
                digit = res % 10
                newNode = ListNode(digit)
                current.next = newNode
                current = newNode
                res = res // 10

        return head.next