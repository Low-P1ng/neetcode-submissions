class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adjl = {i:[0]*len(points) for i in range(len(points))}
        for i in range(len(points)):
            for j in range(len(points)):
                if i==j:
                    adjl[i][j] = [0,i]
                    continue
                md = abs(points[j][0]-points[i][0]) + abs(points[j][1]-points[i][1])
                adjl[i][j] = [md, j]

        visited = set()
        cost = 0
        heap = [[0,0]]
        while len(visited)!=len(points):
            dis, point = heapq.heappop(heap)
            if point in visited:
                continue
            cost += dis
            visited.add(point)
            for elem in adjl[point]:
                if elem[1] not in visited:
                    heapq.heappush(heap, elem)

        return cost


        

        
