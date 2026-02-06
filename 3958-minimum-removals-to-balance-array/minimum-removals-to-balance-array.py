class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        if nums[0] * k >= nums[-1]:
            return 0
        
        n = len(nums)
        ans = n
        l = 0

        for i,v in enumerate(nums):
            while l < i and nums[l] * k < v:
                l += 1
            ans = min(ans, n-i+l-1)
        
        return ans