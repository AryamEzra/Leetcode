class Solution:
    def bitwiseComplement(self, n: int) -> int:
        x = bin(n)[2:]
        ans = ""
        for c in x:
            if c == "1":
                ans += "0"
            else:
                ans += "1"
        return int(ans, 2)
        