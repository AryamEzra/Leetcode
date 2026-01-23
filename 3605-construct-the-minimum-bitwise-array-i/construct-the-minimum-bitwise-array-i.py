class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []
        for n in nums:
            v = -1
            for j in range(1,n):
                if (j|j+1) == n:
                    v = j
                    break
            ans.append(v)
        
        return ans