class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        memo = [-1] * (amount + 1)

        def dfs(amount):
            if amount == 0:
                return 0
            
            res = 10000000
            
            if memo[amount] != -1:
                return memo[amount]

            for coin in coins:
                if amount >= coin:
                    res = min(res, 1 + dfs(amount - coin))

            memo[amount] = res
            return memo[amount]
        
        memo[amount] = dfs(amount)
        return -1 if memo[amount] >= 10000000 else memo[amount]