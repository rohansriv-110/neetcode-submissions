
from typing import List

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # Step 1: Initialize graph with every character
        adj = {c: set() for word in words for c in word}

        # Step 2: Build graph from adjacent words
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]

            # Invalid prefix case
            if len(w1) > len(w2) and w1.startswith(w2):
                return ""

            # Find first differing character
            for j in range(min(len(w1), len(w2))):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break

        # Step 3: DFS with cycle detection
        visit = {}
        res = []

        def dfs(c):
            if c in visit:
                return visit[c]

            # True = currently exploring
            visit[c] = True

            for nei in adj[c]:
                if dfs(nei):
                    return True

            # False = finished exploring
            visit[c] = False
            res.append(c)
            return False

        # Step 4: Process every character
        for c in adj:
            if dfs(c):
                return ""

        # Step 5: Reverse topological order
        res.reverse()
        return "".join(res)
