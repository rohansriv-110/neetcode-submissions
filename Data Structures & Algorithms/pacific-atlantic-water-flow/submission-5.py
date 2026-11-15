
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pacific, atlantic = set(), set()

        def dfs(r, c, visit):
            visit.add((r, c))

            directions = [
                (-1, 0),
                (1, 0),
                (0, -1),
                (0, 1)
            ]

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if 0 <= nr < ROWS and 0 <= nc < COLS:
                    if (nr, nc) not in visit:
                        if heights[nr][nc] >= heights[r][c]:
                            dfs(nr, nc, visit)

        for c in range(COLS):
            dfs(0, c, pacific)
            dfs(ROWS - 1, c, atlantic)

        for r in range(ROWS):
            dfs(r, 0, pacific)
            dfs(r, COLS - 1, atlantic)

        return [list(cell) for cell in pacific & atlantic]
