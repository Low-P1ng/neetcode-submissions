class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dist(x,y):
            return (x*x + y*y) * 0.5
        
        distances = [[dist(x,y),x,y] for x,y in points]
        heapq.heapify(distances)
        res = []
        for i in range(k):
            dis,x,y = heapq.heappop(distances)
            res.append([x,y])

        return res