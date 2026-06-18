class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjl = {i:[] for i in range(1,n+1)}
        for u,v,t in times:
            adjl[u].append([t,v])
        time = 0

        heap = [(0,k)]
        visited = set()
        while heap:
            t1, n1 = heapq.heappop(heap)
            if n1 in visited:
                continue

            visited.add(n1)
            time = max(time,t1)
            for t,nei in adjl[n1]:
                if nei not in visited:
                    heapq.heappush(heap,(t1+t,nei))
        return time if (len(visited) == n) else -1





