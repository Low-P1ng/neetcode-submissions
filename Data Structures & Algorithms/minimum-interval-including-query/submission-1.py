class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        check = defaultdict(list)
        for i,q in enumerate(queries):
            check[q].append(i)

        queries.sort();intervals.sort()
        res = [0]*len(queries)
        j = 0
        heap = []
        for q in queries:
            i = j
            while i < len(intervals):
                if intervals[i][0] <= q <= intervals[i][1]:
                    heapq.heappush(heap, [intervals[i][1]-intervals[i][0]+1,intervals[i][1]])
                i+=1
            while heap and heap[0][1] < q:
                heapq.heappop(heap)
            if not heap:
                for idx in check[q]:
                    res[idx] = -1
            else:
                for idx in check[q]:
                    res[idx] = heap[0][0]

        return res