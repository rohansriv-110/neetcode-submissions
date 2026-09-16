class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for x, y in points:
            dist = (x ** 2) + (y ** 2)        # ✅ yours
            minHeap.append([dist, x, y])      # ✅ yours

        heapq.heapify(minHeap)                    # 🏔️ blank 1: pile the cards

        res = []
        while k > 0:
            dist, x, y = heapq.heappop(minHeap)   # ✅ yours
            res.append([x, y])                    # ✅ yours
            k -= 1                                # ✅ yours

        return res                      # 🎁 blank 2: the collected locations