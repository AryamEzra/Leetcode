class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1 and n not in seen:
            seen.add(n)
            n = str(n)
            ans = 0
            for num in n:
                ans += int(num) ** 2
            print(ans)
            n = ans
        if n == 1:  
            return True
        else:
            return False
        