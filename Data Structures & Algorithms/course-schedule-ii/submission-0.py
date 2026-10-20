class Solution:
    def findOrder(self, numCourses, prerequisites):
        prereq = { c: [] for c in range(numCourses) }
        for crs, pre in prerequisites:
            prereq[crs].append(pre)

        output = []
        visit, cycle = set(), set()      # visit = done, cycle = current path

        def dfs(crs):
            if crs in cycle:
                return False             # looped
            if crs in visit:
                return True              # already in output

            cycle.add(crs)               # step on
            for pre in prereq[crs]:
                if dfs(pre) == False:
                    return False
            cycle.remove(crs)            # step off
            visit.add(crs)               # mark done
            output.append(crs)           # write it down
            return True

        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return output