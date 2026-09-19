# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> list[list[int]]:
        result = []
        def dfs(node, curSum, path):
            if not node:
                return

            path.append(node.val)
            curSum += node.val

            if not node.left and not node.right:
                if curSum == targetSum:
                    result.append(path[:])
            else:
                dfs(node.left, curSum, path)
                dfs(node.right, curSum, path)

            path.pop()
        
        dfs(root, 0, [])
        return result