class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = [[tasks[i][0],i,tasks[i][1]] for i in range(len(tasks))]
        tasks.sort(key=lambda x:x[0])
        tasks = deque(tasks)
        minheap = []
        t = tasks[0][0]
        res = []
        while tasks or minheap:
            if not minheap and t < tasks[0][0]:
                t = tasks[0][0]
            while tasks and tasks[0][0] <= t:
                enq, i, pt = tasks.popleft()
                heapq.heappush(minheap,[pt,i])

            pt,i=heapq.heappop(minheap)
            t+=pt
            res.append(i)
        
        return res
            
