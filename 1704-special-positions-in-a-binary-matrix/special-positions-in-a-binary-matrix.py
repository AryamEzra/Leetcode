class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        count = 0
        r, c = len(mat), len(mat[0])

        for i in range(r):
            for j in range(c):
                if mat[i][j] == 1:
                    row_zero = 0
                    for k in range(r):
                        if mat[k][j] == 0:
                            row_zero += 1
                    
                    col_zero = 0
                    for k in range(c):
                        if mat[i][k] == 0:
                            col_zero += 1
                    # print(row_zero, col_zero, r, c)
                    
                    if col_zero == c - 1 and row_zero == r - 1:
                        count += 1
        
        return count

        