class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        if len(hand)%groupSize != 0:
            return False
        if groupSize == 1:
            return True
        for i in range(len(hand)//groupSize):
            start = hand[0]
            hand.remove(start)
            for j in range(groupSize-1):
                if start+1 not in hand:
                    return False
                start += 1
                hand.remove(start)
        return True
