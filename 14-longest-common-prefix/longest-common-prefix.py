class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        l = float('inf')
        for c in strs:
            if len(c) < l:
                l = len(c)
        # print(l)
        ans = ""
        r,c = len(strs), l

        for j in range(c):
            flag = True
            i = 0
            for i in range(r-1):
                if strs[i][j] != strs[i+1][j]:
                    return ans
            else:
                cur = i
            if flag:
                ans += strs[cur][j]     
        
        return ans
        