class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid),len(grid[0])
        heap = [(grid[0][0],0,0)]
        visited = set()

        def add(t,r,c):
            if (r < 0 or r >= rows or
                c < 0 or c >= cols or
                (r,c) in visited) :
                return
            heapq.heappush(heap,(max(t, grid[r][c]),r,c))
        while heap:
            t,r,c = heapq.heappop(heap)

            if (r,c) in visited:
                continue
            if r==rows-1 and c==cols-1:
                return t
            visited.add((r,c))
            add(t,r+1,c)
            add(t,r-1,c)
            add(t,r,c+1)
            add(t,r,c-1)
