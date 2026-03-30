class Solution:
    def tribonacci(self, n: int) -> int:

        def fib(n: int, memo={0: 0, 1: 1, 2: 1}) -> int:
            if n in memo:
                return memo[n]
            
            memo[n] = fib(n - 1) + fib(n - 2) + fib(n - 3)

            return memo[n]
        
        return fib(n)

        