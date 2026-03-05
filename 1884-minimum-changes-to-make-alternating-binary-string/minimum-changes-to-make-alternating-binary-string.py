class Solution:
    def minOperations(self, s: str) -> int:
        one_start, zero_start =  0, 0
        n = len(s)
        for i in range(n):
            if (i % 2 == 0 and s[i] == '0') or (i % 2 == 1 and s[i] == '1'):
                one_start += 1
        
        for i in range(n):
            if (i % 2 == 0 and s[i] == '1') or (i % 2 == 1 and s[i] == '0'):
                zero_start += 1
        
        # print(one_start, zero_start)
        
        return min(one_start, zero_start)


        