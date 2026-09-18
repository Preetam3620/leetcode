class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i, j = 0, len(matrix[0]) - 1
        while i < len(matrix) and j >= 0:
            val = matrix[i][j]
            if target == val:
                return True
            elif target < val:
                j -= 1
            else:
                i += 1
        return False