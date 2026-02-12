class Solution:
    def longestBalanced(self, s: str) -> int:
        ans = 0
        len_s = len(s)

        for l in range(len_s):
            count = {}
            for r in range(l, len_s):
                count[s[r]] = count.get(s[r], 0) + 1
                freq = set(count.values())

                if len(freq) == 1:
                    ans = max(ans, r - l + 1)
            
        return ans
          