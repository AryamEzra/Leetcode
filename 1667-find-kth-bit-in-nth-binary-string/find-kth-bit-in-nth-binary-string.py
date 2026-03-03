class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def reverse(s):
            return s[::-1]
        
        def invert(s):
            return ''.join('1' if c == '0' else '0' for c in s)
        
        s = "0"
        for i in range(1, n):
            s = s + "1" + reverse(invert(s))
        
        return s[k - 1]