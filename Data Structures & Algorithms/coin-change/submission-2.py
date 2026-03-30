class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Initialize DP array with a value larger than any possible answer
        # float('inf') or amount + 1 works perfectly
        dp = [amount + 1] * (amount + 1)
        
        # Base case: 0 coins are needed to make amount 0
        dp[0] = 0
        
        # Fill the DP table
        for coin in coins:
            for i in range(coin, amount + 1):
                # The min coins for 'i' is the minimum of:
                # 1. Its current value
                # 2. 1 coin (the current one) + result for (i - coin)
                dp[i] = min(dp[i], dp[i - coin] + 1)
        
        # If the value is still the initial placeholder, it's impossible
        return dp[amount] if dp[amount] != amount + 1 else -1
