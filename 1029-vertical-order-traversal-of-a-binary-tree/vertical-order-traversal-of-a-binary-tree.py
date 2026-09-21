# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []

        q = deque([(root, 0, 0)])
        max_col, min_col = 0, 0
        nodes_map  = defaultdict(list)
        while q:
            node, row, col = q.popleft()
            nodes_map[col].append((row, node.val))

            min_col, max_col = min(min_col, col), max(max_col, col)
            
            if node.left:
                q.append((node.left, row + 1, col - 1))
            if node.right:
                q.append((node.right, row + 1, col + 1))
        print(nodes_map)  
        result = []
        for col in range(min_col, max_col + 1):
            nodes_map[col].sort(key=lambda x: (x[0], x[1]))
            col_values = [val for row, val in nodes_map[col]]
            result.append(col_values)
        return result