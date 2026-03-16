class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        heap = []
        nr, nc = len(grid), len(grid[0])
        seen = set()

        for row in range(nr):
            for col in range(nc):
                if grid[row][col] not in seen:
                    seen.add(grid[row][col])
                    heapq.heappush(heap, grid[row][col])
                
                d = 1
                while True:
                    top_r, top_c = row - d, col
                    bot_r, bot_c = row + d, col
                    left_r, left_c = row, col - d
                    right_r, right_c = row, col + d
                    if top_r < 0 or bot_r >= nr or left_c < 0 or right_c >= nc:
                        break
                    
                    summ = 0
                    for i in range(d + 1):
                        summ += grid[top_r + i] [top_c - i]
                    for i in range(1, d + 1):
                        summ += grid[top_r + i] [top_c + i]
                    for i in range(1, d + 1):
                        summ += grid[right_r + i] [right_c - i]
                    for i in range(1, d):
                        summ += grid[left_r + i] [left_c + i]
                        

                    if summ not in seen:
                        seen.add(summ)
                        heapq.heappush(heap, summ)
                    d += 1
                    

        print(heap)
        while len(heap) > 3:
            heapq.heappop(heap)
        
    
        return sorted(heap, reverse=True)

        