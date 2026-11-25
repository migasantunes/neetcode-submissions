class Solution:
    def climbStairs(self, n: int) -> int:
        # 1 <= n <= 45

        # TopDown
        memo = [-1] * (n + 1)

        def dfs(n):
            if n <= 2:
                memo[n] = n
                return memo[n]

            if memo[n] != -1:
                return memo[n]
        
            memo[n] = dfs(n - 1) + dfs(n - 2)
            return memo[n]

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