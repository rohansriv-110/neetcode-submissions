class Solution:
    def validTree(self, n, edges):
        if not n:
            return True

        adj = { i:[] for i in range(n) }
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        visit = set()
        def dfs(i, prev):
            if i in visit:
                return False

            visit.add(i)
            for j in adj[i]:
                if j == prev:
                    continue
                if not dfs(j, i):
                    return False
            
            return True # Added this to properly return True if the DFS completes without finding a cycle

        return dfs(0, -1) and len(visit) == n # Need to trigger the DFS and check if all nodes were visited