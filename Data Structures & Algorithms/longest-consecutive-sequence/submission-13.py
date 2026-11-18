class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        nums = list(set(nums))
        nums.sort()

        if len(nums) == 1: return 1

        longest = 0
        seq = 1

        for i in range(len(nums) - 1):
            if nums[i] + 1 == nums[i + 1]:
                seq += 1
            else:
                seq = 1
            longest = seq if seq > longest else longest
        
        return longest
        """

        # Correct

        numSet = set(nums)
        longest = 0

        for n in numSet:
            if n-1 not in numSet:
                seq = 1
                while n + seq in numSet:
                    seq += 1
                if longest < seq: longest = seq
            
        return longest