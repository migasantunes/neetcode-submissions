import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # final = []

        # for i in range(0, len(nums)):
        #     temp = nums.copy()
        #     temp.pop(i)
        #     final.append(math.prod(temp))
        
        # return final

        n = len(nums)
        final = [1] * n

        left_prod = 1
        for i in range(0, n):
            final[i] = left_prod
            left_prod *= nums[i]
        
        right_prod = 1
        print(nums)
        for i in range(n-1, -1, -1):
            final[i] *= right_prod
            right_prod *= nums[i]

        return final