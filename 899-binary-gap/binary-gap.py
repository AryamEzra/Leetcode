class Solution:
    def binaryGap(self, n: int) -> int:
        dist = float('-inf')
        b = bin(n)[2:]
        l = len(b)

        prev = 0
        cur = 0
        for r in range(l):
            if b[r] == "1":
                prev = cur
                cur = r 
                dist = max(dist, cur - prev)
        
        return dist

                

        