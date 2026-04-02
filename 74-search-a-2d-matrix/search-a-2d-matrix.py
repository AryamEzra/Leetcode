class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nr, nc = len(matrix), len(matrix[0])

        for r in range(nr):
            if matrix[r][0] <= target <= matrix[r][-1] and target in {c for c in matrix[r]}:
                return True
            
        return False
        