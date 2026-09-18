class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        for i in range(ROWS):
            for j in range(COLS):
                if target == matrix[i][j]:
                    return True
        return False