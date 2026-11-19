class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = defaultdict(int)

        for num in nums:
            freqs[num] += 1

        """
        list_freqs = []
        for num, freq in freqs.items():
            list_freqs.append([freq, num])
        list_freqs.sort()

        output = []
        for i in range(k):
            output.append(list_freqs.pop()[1])
        return output
        """

        heap = []
        for num, freq in freqs.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        output = []
        for _ in range(k):
            output.append(heapq.heappop(heap)[1])

        return output