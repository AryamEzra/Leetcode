class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        ans = float('-inf')
        n2 = len(nums2)
        n1 = len(nums1)

        count_neg_1 = 0
        count_neg_2 = 0
        count_pos_1 = 0
        count_pos_2 = 0
        for n in nums1:
            if n < 0:
                count_neg_1 += 1
            if n > 0:
                count_pos_1 += 1
        
        for n in nums2:
            if n < 0:
                count_neg_2 += 1
            if n > 0:
                count_pos_2 += 1
        
        if (count_neg_1 == n1 and count_pos_2 == n2):
            return max(nums1) * min(nums2)

        if (count_pos_1 == n1 and count_neg_2 == n2):
            return min(nums1) * max(nums2)

        # [0 for _ in range(cols)] for _ in range(rows)
        mat = [[0 for _ in range(n2+1)] for _ in range(n1+1)]
        # print(mat)

        for i in range(n1-1, -1, -1):
            for j in range(n2-1, -1, -1):
                op1 = (nums1[i] * nums2[j]) + mat[i+1][j+1]
                op2 = mat[i][j+1]
                op3 = mat[i+1][j]
                a = max(op1, op2, op3)
                # print(op1, op2, op3)
                mat[i][j] = a 
                ans = max(ans, a)       
    
        return ans

        