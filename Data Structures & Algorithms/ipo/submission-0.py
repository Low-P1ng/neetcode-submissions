class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        minheap = [[x,y] for x,y in zip(capital,profits)]
        maxheap = []
        heapq.heapify(minheap)
        for _ in range(k):
            while minheap and minheap[0][0] <= w:
                c,p = heapq.heappop(minheap)
                heapq.heappush(maxheap, -p)
            if not maxheap:
                break
            w += -heapq.heappop(maxheap)
    
        return w
