class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        
        maxHeap = []
        for n in nums:
            heapq.heappush(maxHeap, -n)

        self.nums = maxHeap
        return

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, -val)

        out = []
        for _ in range(self.k):
            out.append(heapq.heappop(self.nums))
        kth = out[-1]

        for num in out:
            heapq.heappush(self.nums, num)
            
        return -kth
