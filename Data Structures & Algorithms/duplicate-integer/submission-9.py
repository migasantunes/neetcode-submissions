class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # nums -> integer array 
        # if any value is repeated return -> true
        # else return -> false
        size = len(nums)

        # if size == 0 or size == 1:
        #     return False

        # Brute force O(n^2)
        
        # for i in range(size):
        #     for j in range(i+1, size):
        #         if nums[i] == nums[j]:
        #             return True
        # return False

        # Sort O(n)

        nums.sort()
        for i in range(size-1):
            if nums[i] == nums[i+1]:
                return True
        return False
