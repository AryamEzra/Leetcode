class Solution:
    def numSteps(self, s: str) -> int:
        count = 0
        x = int(s,2)
        while x != 1:
            if x % 2 == 1:
                x += 1
            else:
                x = x//2
            count += 1
        return count
        