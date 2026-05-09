# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = [[root, 0]] # [node, height]
        maxHeight = 0
        while stack:
            cur, height = stack.pop()
            maxHeight = max(maxHeight, height)
            
            if cur:
                stack.append([cur.left, height + 1])
                stack.append([cur.right, height + 1])
            
        return maxHeight