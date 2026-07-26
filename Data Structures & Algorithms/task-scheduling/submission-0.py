class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        dic = defaultdict(int)
        for elem in tasks:
            dic[elem]+=1
        
        values = [-x for x in dic.values()]
        heapq.heapify(values)
        q=deque()
        t = 0
        while values or q:
            t += 1

            if q and q[0][1] == t:
                heapq.heappush(values, q.popleft()[0])

            if values:
                freq = heapq.heappop(values) + 1
                if freq:
                    q.append([freq, t + n + 1])


        return t
