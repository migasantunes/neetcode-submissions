class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        print(nums)
        for i, v in enumerate(nums):
            if v > 0: # if it's positive, it's impossible to go to zero
                break
            
            if i > 0 and nums[i-1] == v: # checking repeated
                continue

            l, r = i + 1, len(nums) - 1
            
            while l < r:
                three = nums[l] + nums[r] + v
                if three < 0:
                    l += 1
                elif three > 0:
                    r -= 1
                else:
                    res.append([v, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                
        return res 