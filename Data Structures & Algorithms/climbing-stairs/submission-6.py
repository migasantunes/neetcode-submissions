class Solution:
    def climbStairs(self, n: int) -> int:
        # 1 <= n <= 45

        # TopDown
        memo = [-1] * n

        def dfs(n):
            if n <= 0:
                return 0
            
            elif n <= 2:
                memo[n - 1] = n
                return memo[n - 1]

            if memo[n - 1] != -1:
                return memo[n - 1]
            
            else:
                memo[n - 1] = dfs(n - 1) + dfs(n - 2)
                return memo[n - 1]

        return dfs(n)

        # BottomUp
        # if n == 1:
        #     return 1
        # if n == 2:
        #     return 2

        # memo = [0] * n

        # memo[0] = 1
        # memo[1] = 2

        # for i in range(2, n):
        #     memo[i] = memo[i-1] + memo[i-2]
        
        # return memo[n-1]