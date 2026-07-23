class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        
        for num in numSet:
            if num - 1 in numSet:
                continue
            
            streak = 1
            
            while (num + 1 in numSet):
                streak += 1
                num += 1

            if longest < streak:
                longest = streak 

        
        return(longest)