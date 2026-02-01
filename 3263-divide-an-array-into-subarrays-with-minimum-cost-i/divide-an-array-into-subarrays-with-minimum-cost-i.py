class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 3:
            return sum(nums)
        min1 = float('inf')
        min2 = float('inf')

        for v in range(1,n):
            if nums[v] < min1:
                min2 = min1
                min1 = nums[v]
            elif nums[v] < min2:
                min2 = nums[v]
            
        return nums[0] + min1 + min2
        
        
