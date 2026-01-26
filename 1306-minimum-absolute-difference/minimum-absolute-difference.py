class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        graph = defaultdict(list)
        m = float('inf')
        l = len(arr)

        for i in range(l-1):
            diff = arr[i+1] - arr[i]
            graph[diff].append([arr[i], arr[i+1]])
            m = min(diff, m)
        
        return graph[m]