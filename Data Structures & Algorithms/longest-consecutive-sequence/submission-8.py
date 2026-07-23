class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in numSet:
            if num - 1 in numSet:
                continue
            
            streak = 1
            
            while (num + streak in numSet):
                streak += 1

            longest = max(streak, longest)

        
        return(longest)