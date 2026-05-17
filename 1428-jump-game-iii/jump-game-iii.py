class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        # time: O(n)
        # space: O(n)

        #bfs

        n = len(arr)
        visited = [False] * n
        queue = deque([start])
        visited[start] = True

        while queue:
            i = queue.popleft()
            if arr[i] == 0:
                return True
            
            jump = arr[i]

            f = i + jump
            if 0 <= f < n and not visited[f]:
                visited[f] = True
                queue.append(f)

            back = i - jump 
            if 0 <= back < n and not visited[back]:
                visited[back] = True
                queue.append(back)
        

        return False
