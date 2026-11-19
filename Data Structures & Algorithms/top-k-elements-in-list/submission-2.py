class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = defaultdict(int)

        for num in nums:
            freqs[num] += 1

        list_freqs = []
        for num, freq in freqs.items():
            list_freqs.append([freq, num])
        list_freqs.sort()

        output = []
        for i in range(k):
            output.append(list_freqs.pop()[1])
        return output