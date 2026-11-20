class Solution:
    def climbStairs(self, n: int) -> int:
        # Top Down DP
        # cache = [-1] * n

        # def dfs(i):
        #     if i >= n:
        #         return i == n
            
        #     if cache[i] != -1:
        #         return cache[i]
            
        #     cache[i] = dfs(i + 1) + dfs(i + 2)
        #     return cache[i]
        
        # return dfs(0)

        # Bottom Up DP
        if n <= 2:
            return n

        res = [0] * n
        res[0], res[1] = 1, 2

        for i in range(2, n):
            res[i] = res[i - 1] + res[i - 2]
        
        return res[n - 1]