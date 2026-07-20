class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        freq = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            count[num] += 1

        for num, times in count.items():
            freq[times].append(num)
        
        final = list()
        for numList in freq[::-1]:
            if (numList == None): continue
            for num in numList:
                final.append(num)
                if (len(final) == k):
                    return final