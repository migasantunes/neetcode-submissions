class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Brute Force -> sorting and keeping track of the biggest sequence
        # Using set to check on O(1) if n is the first on the sequence 
        if not nums:
            return 0

        s = set(nums)

        res = 1
        for num in nums:
            if num - 1 in s:
                continue
            
            count = 1
            while num + 1 in s:
                count += 1
                num += 1
            res = max(count, res)

        return res