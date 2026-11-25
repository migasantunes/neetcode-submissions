class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = [] 
        heapq.heapify(heap)

        for xi, yi in points:
            distance = math.sqrt(xi**2 + yi**2)
            heapq.heappush(heap, (-distance, xi, yi))

        while len(heap) > k:
            heapq.heappop(heap)
        
        res = []
        for _ in range(len(heap)):
            distance, x, y = heapq.heappop(heap)
            res.append([x, y])

        return res