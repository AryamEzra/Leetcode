class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        summ = nums[0]
        n = len(nums)
        for i in range(1,n):
            if nums[i] == nums[i-1] + 1:
                summ += nums[i]
            else:
                break
        print(summ)
        check = set(nums)
        if summ not in check:
            return summ
        else:
            while summ in check:
                summ += 1
            return summ

        