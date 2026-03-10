class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        graph = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c)- ord('a')] += 1
            graph[tuple(count)].append(s)
            
        for k,v in graph.items():
            ans.append(v)
        return ans