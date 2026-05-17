class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        # time: O(n)
        # space: O(n)
        n = len(arr)
        visited = [False] * n

        def dfs(i):
            if i < 0 or i >= n or visited[i]:
                return False
            
            if arr[i] == 0:
                return True
            
            visited[i] = True
            jump = arr[i]
            return dfs(i + jump) or dfs(i - jump)
        
        return dfs(start)
        