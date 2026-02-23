class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        check = set()
        for i in range(len(s) - k + 1):
            check.add(s[i:i+k])
        
        return len(check) == 2 ** k
        
        