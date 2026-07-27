class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = [[tasks[i][0],i,tasks[i][1]] for i in range(len(tasks))]
        tasks.sort(key=lambda x:x[0])
        minheap,res = [],[]
        t,i = 0,0
        while i < len(tasks) or minheap:
            if not minheap and i < len(tasks):
                t = max(t, tasks[i][0])
            while i<len(tasks) and tasks[i][0] <= t:
                enq, idx, pt = tasks[i]
                heapq.heappush(minheap,[pt,idx])
                i+=1

            pt,idx=heapq.heappop(minheap)
            t+=pt
            res.append(idx)
        
        return res
            
