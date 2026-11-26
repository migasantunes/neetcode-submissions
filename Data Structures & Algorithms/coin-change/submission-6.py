class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 1 <= coins.length <= 10
        # 1 <= coins[i] <= high
        # 0 <= amount <= 10000

        # TopDown

        memo = [-1] * (amount + 1)

        def dfs(a):
            if a <= 0:
                return 0
            
            if memo[a] != -1:
                return memo[a]
            
            minAmount = amount + 1
            for c in coins:
                if a - c >= 0:
                    minAmount = min(minAmount, 1 + dfs(a - c))
                
            memo[a] = minAmount
            return memo[a]

        minCoins = dfs(amount)
        return -1 if minCoins >= amount + 1 else minCoins