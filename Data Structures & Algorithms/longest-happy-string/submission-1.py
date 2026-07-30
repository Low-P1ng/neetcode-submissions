class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        maxheap = [[-a,'a'],[-b,'b'],[-c,'c']]
        for i in range(len(maxheap) - 1, -1, -1):
            if maxheap[i][0] == 0:
                maxheap.pop(i)
        heapq.heapify(maxheap)
        res = ""
        while maxheap:
            v,k = heapq.heappop(maxheap)
            if len(res)>1 and res[-1] == res[-2] == k:
                if not maxheap:
                    break
                v1,k1 = heapq.heappop(maxheap)
                res+=k1
                v1+=1
                if v1:
                    heapq.heappush(maxheap,[v1,k1])
            else:
                res += k
                v += 1
            if v:
                heapq.heappush(maxheap,[v,k])
                
        return res