class Solution:
    def countTriples(self, n: int) -> int:
        s = []
        for i in range(1, n+1):
            for j in range(i+1, n+1):
                for k in range(i+2, n+1):
                    if i**2 + j **2 == k**2:
                        s.append((i,j,k))
        
        return len(s) * 2
        