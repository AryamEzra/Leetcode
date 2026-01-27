class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        l = len(bits)
        i = 0
        while i < l - 1:
            if bits[i]  == 1:
                i += 2
            else:
                i += 1
        
        return i == l - 1
        