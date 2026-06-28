class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize != 0:
            return False
        if groupSize == 1:
            return True
        dic = defaultdict(int)
        for elem in hand:
            dic[elem] += 1
        minH = list(dic.keys())
        heap = heapq.heapify(minH)
        while minH:
            start = minH[0]
            for i in range(start, start+groupSize):
                if i not in dic:
                    return False
                dic[i] -= 1
                if dic[i] == 0:
                    if i != minH[0]:
                        return False
                    heapq.heappop(minH)
            
        return True
