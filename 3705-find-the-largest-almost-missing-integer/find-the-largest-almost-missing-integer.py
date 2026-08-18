class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        ans = -1
        n = len(nums)
        count = defaultdict(int)
        for i in range(n - k + 1):
            sub = nums[i: i+k]
            for num in set(sub):
                count[num] += 1

        for k,v in count.items():
            if v == 1:
                ans = max(ans, k)

        return ans

        