class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        check = {'r':[],'c':[]}
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    check['r'].append(i)
                    check['c'].append(j)
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in check['r'] or j in check['c']:
                    matrix[i][j] = 0


        