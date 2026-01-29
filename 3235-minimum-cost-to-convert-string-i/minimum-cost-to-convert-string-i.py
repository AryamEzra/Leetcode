class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        adj = defaultdict(list)
        for src, dest, cur_cost in zip(original, changed, cost):
            adj[src].append((dest, cur_cost))
           
        def dijkstra(src): 
            heap = [(0,src)] 
            min_cost_map = {}

            while heap:
                cost, node = heappop(heap)
                if node in min_cost_map:
                    continue
                min_cost_map[node] = cost
                for neigh, neigh_cost in adj[node]:
                    total_neigh_cost = cost + neigh_cost
                    heappush(heap, (total_neigh_cost, neigh))

            return min_cost_map
        
        min_cost_maps = {c: dijkstra(c) for c in set(source)}
        res = 0
        for src, dest in zip(source, target):
            if dest not in min_cost_maps[src]:
                return -1
            res += min_cost_maps[src][dest]

        return res 
        