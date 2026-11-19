class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Max Heap
        maxheap = []
        for i in range(len(prices) - 1):
            for j in range(i + 1, len(prices)):
                heapq.heappush(maxheap, -(prices[j]-prices[i]))
        
        highest = -heapq.heappop(maxheap) if len(maxheap) > 0 else 0

        return max(0, highest)