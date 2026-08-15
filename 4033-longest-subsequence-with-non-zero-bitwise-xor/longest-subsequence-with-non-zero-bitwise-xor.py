class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        ans = nums[0]
        n = len(nums)
        zero = [0] * n
        if zero == nums:
            return 0
        for i in range(1,n):
            ans ^= nums[i]
        
        if ans == 0:
            return n-1
        else:
            return n
        

        