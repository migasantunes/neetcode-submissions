class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Max Heap (just to train, could've just used max())
        """
        maxheap = []
        for i in range(len(prices) - 1):
            for j in range(i + 1, len(prices)):
                heapq.heappush(maxheap, -(prices[j]-prices[i]))
        
        highest = -heapq.heappop(maxheap) if len(maxheap) > 0 else 0

        return max(0, highest)
        """

        l = 0
        r = l + 1
        res = 0
        while r != len(prices):
            if prices[r] <= prices[l]:
                l = r
                r += 1
            else:
                res = max(res, prices[r]-prices[l])
                r += 1
        return res


