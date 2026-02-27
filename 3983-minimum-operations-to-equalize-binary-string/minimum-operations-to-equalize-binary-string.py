class Solution:
    def minOperations(self, s: str, k: int) -> int:
        zero = 0
        l = len(s)
        for i in range(l):
            zero += ~ord(s[i]) & 1

        if zero == 0:
            return 0

        if l == k:
            return 1 if zero == l else -1

        val = l - k
        odd = max(math.ceil(zero / k), math.ceil((l - zero) / val))
        odd += ~odd & 1
        even = max(math.ceil(zero / k), math.ceil(zero / val))
        even += even & 1

        ans = float('inf')

        if (k & 1) == (zero & 1):
            ans = min(ans, odd)

        if (~zero & 1) == 1:
            ans = min(ans, even)

        return -1 if ans == float('inf') else ans
        