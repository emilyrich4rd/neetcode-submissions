class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # transpose by iterating on the diagonals
        # for every diagonal from left top, swap their numbers
        for d in range(len(matrix)):
            for i in range(d+1, len(matrix)):
                temp = matrix[d][i]
                matrix[d][i] = matrix[i][d]
                matrix[i][d] = temp 
        
        for lst in matrix:
            lst.reverse()

        