class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        mapp = defaultdict(list)
        ans = []

        for i in range(len(groupSizes)):
            mapp[groupSizes[i]].append(i)
        # print(mapp)
                    
        
        for k,v in mapp.items():
            if k == len(v):
                ans.append(v)
            else:
                for i in range(0,len(v)-k+1,k):
                    cur = v[i:i+k]
                    print(cur)
                    ans.append(cur)
            
        return ans
        
        

        