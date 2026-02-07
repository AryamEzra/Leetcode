class Solution:
    def minimumDeletions(self, s: str) -> int:
        #t:O(n)
        #s:
        l = len(s)
        a_count_right = [0] * l

        # [3, 2, 2, 1, 1, 1, 0, 0]
        for i in range(l-2, -1, -1):
            a_count_right[i] = a_count_right[i+1]
            if s[i+1] == "a":
                a_count_right[i] += 1
        # print(a_count_right)

        b_count_left = 0
        res = len(s)
        for i,c in enumerate(s):
            res = min(res, b_count_left + a_count_right[i])
            if c == "b":
                b_count_left += 1
        
        return res
        

        
        