class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        
        # maxHeap = []
        # for n in nums:
        #     heapq.heappush(maxHeap, -n)

        # self.nums = maxHeap

        self.heap = nums
        heapq.heapify(self.heap)
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        # heapq.heappush(self.nums, -val)

        # out = []
        # for _ in range(self.k):
        #     out.append(heapq.heappop(self.nums))
        # kth = out[-1]

        # for num in out:
        #     heapq.heappush(self.nums, num)
            
        # return -kth

        heapq.heappush(self.heap, val)
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]