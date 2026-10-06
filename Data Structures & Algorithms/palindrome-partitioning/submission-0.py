class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, part = [], []

        def dfs(i):
            if i >= len(s):                      # whole string cut → save copy
                res.append(part.copy())
                return
            for j in range(i, len(s)):           # try every end for this piece
                if self.isPali(s, i, j):         # only palindrome pieces
                    part.append(s[i:j + 1])      # choose
                    dfs(j + 1)                   # explore rest
                    part.pop()                   # undo

        dfs(0)
        return res

    def isPali(self, s, l, r):
        while l < r:                             # squeeze inward
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True