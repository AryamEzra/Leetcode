class Solution:
    def reverseBits(self, n: int) -> int:
        s = bin(n)[2:]
        if len(s) != 32:
            s = '0' * (32-len(s)) + s
        ans = []
        for c in s:
            ans.append(c)
        ans = ans[::-1]
        s = "".join(ans)
        return int(s,2)

        