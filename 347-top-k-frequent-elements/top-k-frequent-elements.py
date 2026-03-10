class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        count_sort = sorted(count.items(), key=lambda item: item[1], reverse = True)
        ans = []
        for key,v in count_sort:
            ans.append(key)
            if len(ans) == k:
                break
        return ans
        