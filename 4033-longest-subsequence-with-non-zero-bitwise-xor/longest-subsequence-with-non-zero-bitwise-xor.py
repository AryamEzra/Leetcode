class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        zero = nums.count(0)
        ans = nums[0]
        n = len(nums)
        if zero == n:
            return 0
        for i in range(1,n):
            ans ^= nums[i]
        
        if ans == 0:
            return n-1
        else:
            return n
        

        