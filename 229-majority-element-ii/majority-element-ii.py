class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        from collections import Counter
        count = Counter(nums)
        n = math.floor(len(nums)/3)
        ans = []
        for k,v in count.items():
            if v > n:
                ans.append(k)
        return ans