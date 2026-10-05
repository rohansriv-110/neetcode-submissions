class Solution:
    def subsetsWithDup(self, nums):
        nums.sort()
        res, subset = [], []

        def backtrack(start):
            res.append(subset[:])
            for j in range(start, len(nums)):
                if j > start and nums[j] == nums[j - 1]:
                    continue
                subset.append(nums[j])
                backtrack(j + 1)
                subset.pop()

        backtrack(0)
        return res