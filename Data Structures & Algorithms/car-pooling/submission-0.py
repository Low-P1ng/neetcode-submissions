class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda x: x[1])
        minheap = []
        current = 0
        for p,u,v in trips:
            while minheap and minheap[0][0] <= u:
                u1,p1 = heapq.heappop(minheap)
                current -= p1

            current += p
            if current > capacity:
                return False

            heapq.heappush(minheap, [v,p])
        return True
 
