class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        ans = k - 1
        if ans == 0:
            return True

        for i in range(k+1, n):
            if nums[i] > nums[i-1] and nums[i-k] > nums[i-k-1]:
                ans -=1
            else:
                ans = k -1
            if ans == 0:
                return True
        
        return False
        

        