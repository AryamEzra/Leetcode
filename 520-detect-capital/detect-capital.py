class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        count = 0
        for c in word:
            if 65 <= ord(c) <= 90:
                count += 1
        
        if count == len(word) or count == 0:
            return True
        if count == 1 and 65 <= ord(word[0]) <= 90:
            return True

        return False
        