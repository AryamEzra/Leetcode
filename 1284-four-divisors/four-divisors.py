class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        ans = 0
        
        for n in nums:
            l = set()
            for i in range(1, int(sqrt(n)) + 1):
                if n % i == 0:
                    l.add(i)
                    l.add(n//i)

            if len(l) == 4:
                for j in l:
                    ans += j
        return ans