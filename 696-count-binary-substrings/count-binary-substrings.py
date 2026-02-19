class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        l = len(s)
        ans = 0
        cur = 1
        prev = 0

        for i in range(1,l):
            if s[i] == s[i-1]:
                cur += 1
            else:
                ans = ans + min(cur, prev)
                prev = cur 
                cur = 1
        ans += min(cur, prev)
        return ans
                

        