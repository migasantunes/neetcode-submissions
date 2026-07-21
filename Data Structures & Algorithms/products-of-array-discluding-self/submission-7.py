import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        final = []

        for i in range(0, len(nums)):
            temp = nums.copy()
            temp.pop(i)
            final.append(math.prod(temp))
        
        return final