class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        
        # attempt 5: simulating - 2,2,-1,3,-2,2,1,1,1,0,-1
        #1. 2,2,-1,3,-2,2,1,1,1,-1
        #2. 2,2,-1,3,0,1,1,1,-1
        #3. 2,2,-1,3,0,1,1,0
        #4. 2,1,3,0,1,1,0
        #5. 2,1,3,1,1,0
        #6. 2,1,3,1,1
        #7. 2,1,3,2
        #8. 3,3,2
        #9. 3,5


        n = len(nums)
        count = 0
        while nums != sorted(nums):
            min_sum = float('inf')
            min_idx = -1

            for i in range(len(nums)-1):
                if nums[i] + nums[i+1] < min_sum: # the not equal sign insures I get the first left most min
                    min_sum = nums[i] + nums[i+1]
                    min_idx = i
            

            nums[min_idx] = min_sum
            del nums[min_idx + 1]
            count += 1 


        return count

