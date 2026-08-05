from collections import deque

class Solution:
    def hasValidPath(self, grid: list[list[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        directions = {
            1: [(0, -1), (0, 1)],
            2: [(-1, 0), (1, 0)],
            3: [(0, -1), (1, 0)],
            4: [(0, 1), (1, 0)],
            5: [(0, -1), (-1, 0)],
            6: [(0, 1), (-1, 0)],
        }

        visited = [[False] * n for _ in range(m)]
        queue = deque([(0, 0)])
        visited[0][0] = True

        while queue:
            curr_x, curr_y = queue.popleft()

            if curr_x == m - 1 and curr_y == n - 1:
                return True

            for dx, dy in directions[grid[curr_x][curr_y]]:
                nx, ny = curr_x + dx, curr_y + dy
                if nx < 0 or nx >= m or ny < 0 or ny >= n:
                    continue
                if visited[nx][ny]:
                    continue
                for bx, by in directions[grid[nx][ny]]:
                    if bx == -dx and by == -dy:
                        visited[nx][ny] = True
                        queue.append((nx, ny))
                        break

        return False