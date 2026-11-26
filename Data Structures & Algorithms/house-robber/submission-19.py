class Solution:
    def rob(self, nums: List[int]) -> int:
        # 1 <= nums.length <= 100
        # 0 <= nums[i] <= 100

        memo = [-1] * (len(nums) + 1)


        def dfs(house):
            if house > len(nums):
                return 0

            if memo[house] != -1:
                return memo[house]
            
            memo[house] = max(nums[house - 1] + dfs(house + 2), dfs(house + 1))
            return memo[house]
        
        return dfs(1)