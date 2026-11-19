
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROW, COLS = len(grid), len(grid[0])
        visit = set()
        islands = 0

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r, c):
            visit.add((r, c))

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if (0 <= nr < ROW and
                    0 <= nc < COLS and
                    grid[nr][nc] == "1" and
                    (nr, nc) not in visit):

                    dfs(nr, nc)

        for r in range(ROW):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visit:
                    dfs(r, c)
                    islands += 1

        return islands
