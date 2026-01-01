class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ""
        for v in digits:
            s += str(v)
        print(s)

        x = int(s) + 1
        l = str(x)

        ans = []
        for c in l:
            ans.append(int(c))
        
        return ans

