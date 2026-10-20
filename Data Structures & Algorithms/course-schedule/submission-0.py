class Solution:
    def canFinish(self, numCourses, prerequisites):
        preMap = {i: [] for i in range(numCourses)}   # course → prerequisites
        for crs, pre in prerequisites:
            preMap[crs].append(pre)                   # crs needs pre

        visitSet = set()                              # courses on the CURRENT path

        def dfs(crs):
            if crs in visitSet:
                return False                          # looped back → impossible
            if preMap[crs] == []:
                return True                           # nothing left to do

            visitSet.add(crs)                         # step onto the path
            for pre in preMap[crs]:
                if not dfs(pre): return False         # recurse on the NEIGHBOUR
            visitSet.remove(crs)                      # step back off (backtrack)
            preMap[crs] = []                          # cache: proven fine
            return True

        for crs in range(numCourses):
            if not dfs(crs): return False             # graph may be disconnected
        return True