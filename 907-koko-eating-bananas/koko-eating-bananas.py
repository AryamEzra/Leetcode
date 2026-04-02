class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
       
        l = 1
        r = max(piles)

        def helper(mid):
            t = 0
            for p in piles:
                t += math.ceil(p/mid)
            
            if t <= h:
                return True
            return False

        while l < r:
            mid = (l+r) // 2
            if helper(mid):
                r = mid 
            else:
                l = mid + 1
            
        return l
        