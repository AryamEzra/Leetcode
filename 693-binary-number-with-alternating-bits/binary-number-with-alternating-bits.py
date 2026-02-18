class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        b = bin(n)[2:]
        l = len(b)
        for i in range(l-1):
            if b[i] == b[i+1]:
                return False
        
        return True
        