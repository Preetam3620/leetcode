# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        if not root:
            return False
        stack = [[root, root.val]]
        result = 0
        while stack:
            node, totalSum = stack.pop()
            if node.left == None and node.right == None and totalSum == targetSum:
                return True
            if node.left:
                stack.append([node.left, totalSum + node.left.val])
            if node.right:
                stack.append([node.right, totalSum + node.right.val])

        return False