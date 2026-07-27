class Solution:
    def reorganizeString(self, s: str) -> str:
        dic = defaultdict(int)
        for elem in s:
            dic[elem]+=1
        
        maxheap = [[-v,k] for k,v in dic.items()]
        heapq.heapify(maxheap)
        store = None
        res=""
        while maxheap:
            v,k = heapq.heappop(maxheap)
            res+=k
            if store:
                heapq.heappush(maxheap, store)
                store = None
            if v+1 < 0:
                store = [v+1,k]

        if store:
            return ""
        return res
            

            
