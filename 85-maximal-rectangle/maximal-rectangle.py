class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        # https://www.youtube.com/watch?v=g8bSdXCG-lA

        def largest_rectangle_area(heights):
            stack = []
            max_area = 0
            n = len(heights)

            for i, h in enumerate(heights):
                start = i
                while stack and stack[-1][0] > h:
                    height, idx = stack.pop()
                    max_area = max(max_area, height * (i - idx))
                    start = idx
                stack.append((h, start))

            while stack:
                height, idx = stack.pop()
                max_area = max(max_area, height * (n - idx))

            return max_area

        max_area = 0
        area = 0
        cur = [0] * len(matrix[0])
        r,c = len(matrix), len(matrix[0])

        for i in range(r):
            for j in range(c):
                if matrix[i][j] == '1':
                    cur[j] += 1
                else:
                    cur[j] = 0
            
            area = largest_rectangle_area(cur)
            if area > max_area:
                max_area = area
            
        return max_area
                

            
            
        