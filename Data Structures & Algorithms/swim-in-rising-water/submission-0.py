
import heapq
from typing import List

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        visit = {(0, 0)}
        minH = [[grid[0][0], 0, 0]]
        res = 0

        directions = [[0, -1], [0, 1], [1, 0], [-1, 0]]

        while minH:
            t, r, c = heapq.heappop(minH)
            res = max(res, t)

            if r == N - 1 and c == N - 1:
                return res

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if nr < 0 or nc < 0 or nr >= N or nc >= N:
                    continue

                if (nr, nc) in visit:
                    continue

                visit.add((nr, nc))
                heapq.heappush(minH, [grid[nr][nc], nr, nc])
