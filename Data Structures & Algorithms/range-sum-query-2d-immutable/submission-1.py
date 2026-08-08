class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.rows = len(matrix)
        self.cols = len(matrix[0])
        self.precompute = [[0]*(self.cols+1) for j in range(self.rows+1)]
        for r in range(self.rows):
            prefix = 0
            for c in range(self.cols):
                prefix += matrix[r][c]
                self.precompute[r+1][c+1] = prefix + self.precompute[r][c+1]
        print(self.precompute)

    def sumRegion(self, r1: int, c1: int, r2: int, c2: int):
        return self.precompute[r2+1][c2+1] - self.precompute[r1][c2+1] - self.precompute[r2+1][c1] + self.precompute[r1][c1]
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)