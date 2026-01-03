class Solution:
    def numOfWays(self, n: int) -> int:
        mod = 10 ** 9  + 7
        aba = 6
        abc = 6

        for i in range(2,n+1):
            temp = abc
            abc = (2 * aba + 2 * abc) % mod
            aba = (3 * aba + 2 * temp) % mod
        
        return (abc + aba) % mod



        