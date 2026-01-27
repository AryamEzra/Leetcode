class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        l = len(bits)
        i = 0
        while i < l - 1:
            i += bits[i] + 1
        
        return i == l - 1
        