class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        count = Counter(nums)
        n = len(nums) // 2
        for k,v in count.items():
            if v == n:
                return k