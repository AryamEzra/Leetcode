class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        l = len(s)
        count = 0
        cur = 0

        for i in range(l):
            if s[i] == "1":
                count += 1
            else:
                cur = i
                break
        # print(count, cur)
        
        if count > 0 and cur > 0:
            for j in range(cur, l):
                if s[j] == "1":
                    return False
        
        return True
        