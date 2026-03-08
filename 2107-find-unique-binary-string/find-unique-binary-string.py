class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        if n == 1:
            if nums[0] == "0":
                return "1"
            else:
                return "0"

        check = set(nums)
        for i in range(n**2):
            x = bin(i)[2:]
            if len(x) < n:            
                x = "0" * (n - len(x)) + x 

            if x not in check:
                return x
        