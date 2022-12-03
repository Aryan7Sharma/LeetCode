class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sums = 0
        sd = len(mat[0])-1
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if i==j:
                    sums+=mat[i][j]
                elif sd==j:
                    sums+=mat[i][j]
            sd-=1
        return sums