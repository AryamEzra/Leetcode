class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        #position of the chars matters that's why we can't just remove d and e for the example delete and leet we need to keep in mind the subsequence - which makes it dp, I thought traversing through both by comparing the chars would work but I do not know which speicific chars I'll need to delete because it's a subsequence so the order matters 
        
        # a min question usually is optimiztion which means either greedy or dp and since it's subsequence better to do dp
        
        @cache
        def dp(i,j):
            if i < 0 and j < 0:
                return 0
            if i < 0:
                return  dp(i, j-1) + ord(s2[j])
            if j < 0:
                return  dp(i-1, j) + ord(s1[i])
                
            if s1[i] == s2[j]:
                return dp(i-1, j-1)
            else:
                op1 = dp(i-1, j) + ord(s1[i]) # delete from s1 and increment it's ascii 
                op2 = dp(i, j-1) + ord(s2[j]) 
                return min(op1, op2)

        return dp(len(s1)-1, len(s2)-1)
        