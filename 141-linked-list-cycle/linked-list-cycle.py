# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hashMap = defaultdict(int)
        
        while head:
            if head in hashMap:
                return True
            hashMap[head] = head.val
            head = head.next
        return False