class Solution:
    def rob(self, nums: List[int]) -> int:
        # rob house 1 -> rob house 3 or rob house 4
        # 1 2 3 4 or 1 2 3 4
        # ^   ^      ^     ^
        cache = [-1] * len(nums) 

        # TopDown
        def dfs(h):
            if h >= len(nums):
                return 0
            
            if cache[h] != -1:
                return cache[h]
            
            cache[h] = nums[h] + max(dfs(h + 2), dfs(h + 3)) 
            return cache[h]

        if len(nums) == 1: return nums[0]
        
        cache[0] = dfs(0)
        cache[1] = dfs(1)
        return max(cache[0], cache[1])
        
        # BottomUp
        # leng = len(nums)
        
        # if leng == 0:
        #     return 0
        
        # if leng == 1:
        #     return nums[0]
        # if leng == 2:
        #     return max(nums[1], nums[0])
        
        # nums[2] = nums[2] + nums[0]
        # if leng == 3:
        #     return max(nums[2], nums[1])
        
        # for i in range(3, leng):
        #     nums[i] += max(nums[i - 2], nums[i - 3])
        
        # return max(nums[leng - 1], nums[leng - 2])

