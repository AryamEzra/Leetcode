class Solution:
    def climbStairs(self, n: int) -> int:
        # dp
        # time: O(n)
        # space: O(n)

        cache = {}

        def dp(n):
            if n in cache:
                return cache[n]
            if n == 1:
                return 1
            if n == 2:
                return 2

            
            cache[n] = dp(n-1) + dp(n-2)
            return cache[n]
        
        return dp(n)
        