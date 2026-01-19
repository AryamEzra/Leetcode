class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        s = sum(apple)
        capacity.sort(reverse = True)

        count = 0
        l = len(capacity)
        
        while s > 0 and count < l:
            s -= capacity[count]
            count += 1
        return count
            
        