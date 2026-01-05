class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        r,c = len(matrix), len(matrix[0])
        l = []
        abs_min = float('inf')

        for i in range(r):
            for j in range(c):
                if matrix[i][j] <= 0:
                   l.append(matrix[i][j])  
                abs_min = min(abs_min, abs(matrix[i][j]))

        ans = 0
        for i in range(r):
            for j in range(c):
                ans += abs(matrix[i][j])
        
        if len(l) % 2 == 0:
            return ans
        else:
            ans -= 2 * abs_min
            return ans
        