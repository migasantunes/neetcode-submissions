class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for x, y in points:
            distance = math.sqrt(math.pow(x, 2) + math.pow(y, 2))
            heapq.heappush(heap, (distance, x, y))
        
        res = []
        for i in range(k):
            d, x, y = heapq.heappop(heap)
            res.append([x, y])
        
        return res