class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # BottomUp

        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if a >= c:
                    dp[a] = min(dp[a], 1 + dp[a - c])
                    
        return dp[amount] if dp[amount] != amount + 1 else -1

        # # TopDown
        # memo = [-1] * (amount + 1)

        # def dfs(amount):
        #     if amount == 0:
        #         return 0
            
        #     if memo[amount] != -1:
        #         return memo[amount]
            
        #     res = 10000000

        #     for coin in coins:
        #         if amount >= coin:
        #             res = min(res, 1 + dfs(amount - coin))

        #     memo[amount] = res
        #     return memo[amount]
        
        # memo[amount] = dfs(amount)
        # return -1 if memo[amount] >= 10000000 else memo[amount]