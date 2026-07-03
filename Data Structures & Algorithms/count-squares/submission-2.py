class CountSquares:

    def __init__(self):
        self.pts = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.pts[tuple(point)] += 1   

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point
        for x,y in tuple(self.pts.keys()):
            if abs(px-x) != abs(py-y) or px == x:
                continue
            if (x,py) and (px,y) in self.pts:
                res += self.pts[(x,py)] * self.pts[(px,y)] * self.pts[(x,y)]
        return res
        
# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)