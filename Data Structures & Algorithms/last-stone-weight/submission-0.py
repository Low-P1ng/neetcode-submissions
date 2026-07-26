class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            x,y = -heapq.heappop(stones), -heapq.heappop(stones)
            if abs(x-y):
                heapq.heappush(stones, -abs(x-y))
        
        return -stones[0] if stones else 0