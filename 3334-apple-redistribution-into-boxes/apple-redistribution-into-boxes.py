class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        s = sum(apple)
        capacity.sort(reverse = True)

        count = 0
        l = len(capacity)
        i = 0
        while s > 0 and i < l:
            count += 1
            s -= capacity[i]
            i += 1
        return count
            
        