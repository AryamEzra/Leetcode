class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = 0

        for i in range(len(nums)):
            if  i + nums[i] > goal and goal >= i:
                goal = i + nums[i]   
        return goal >= len(nums) - 1


    


        