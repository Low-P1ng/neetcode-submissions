class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        t1,t2,t3 = target
        c1,c2,c3 = False, False, False
        for a,b,c in triplets:
            if a>t1 or b>t2 or c>t3:
                continue
            if a == t1:
                c1 = True
            if b == t2:
                c2 = True
            if c == t3:
                c3 = True
        return c1 and c2 and c3