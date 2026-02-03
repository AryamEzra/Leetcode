class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        l = len(nums)
        for i in range(0,l,2):
            ans += nums[i]
        return ans