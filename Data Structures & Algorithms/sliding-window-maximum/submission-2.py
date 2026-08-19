class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = collections.deque()  # stores indices
        l = r = 0

        while r < len(nums):
            # Step A: maintain decreasing order — pop smaller values from the back
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            # Step B: evict front index if it's fallen outside the window
            if l > q[0]:
                q.popleft()

            # Step C: once window reaches size k, record max and slide left edge
            if (r - l + 1) >= k:
                output.append(nums[q[0]])
                l += 1

            r += 1

        return output
