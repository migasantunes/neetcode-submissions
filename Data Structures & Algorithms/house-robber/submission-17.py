class Solution:
    def rob(self, nums: List[int]) -> int:
        # 1 <= nums.length <= 100
        # 0 <= nums[i] <= 100

        cache = [-1] * (len(nums) + 1)


        def dfs(house):
            if house > len(nums):
                return 0
            
            if house == len(nums):
                return nums[house - 1]

            if house == len(nums) - 1:
                return max(nums[len(nums) - 1], nums[len(nums) - 2])

            if cache[house] != -1:
                return cache[house]
            
            cache[house] = max(nums[house - 1] + dfs(house + 2), dfs(house + 1))
            return cache[house]
        
        return dfs(1)