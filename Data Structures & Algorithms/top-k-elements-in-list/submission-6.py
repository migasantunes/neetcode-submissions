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
        """

        buckets = [[] for _ in range(len(nums) + 1)]

        for num, freq in freqs.items():
            buckets[freq].append(num)
        
        output = []
        for i in range(len(buckets)-1,0,-1):
            for num in buckets[i]:
                output.append(num)
                if len(output) == k:
                    return output
