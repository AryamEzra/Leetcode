class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        s = sum(nums)
        n = len(nums)
        cur = 0
        ans = 0
        for i in range(n-1):
            cur += nums[i]
            left = s - cur
            if (cur - left) % 2 == 0:
                ans += 1
                # print(cur, left)
    
        return ans

        