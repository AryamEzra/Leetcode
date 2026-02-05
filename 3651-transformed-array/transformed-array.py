class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        l = len(nums)
        ans = [0] * l
        for i,v in enumerate(nums):
            j = (i + v) % l
            ans[i] = nums[j]
        return ans
        