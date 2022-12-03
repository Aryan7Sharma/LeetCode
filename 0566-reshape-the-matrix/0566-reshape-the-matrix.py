class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m,n=len(mat),len(mat[0])
        if m*n!=r*c:
            return mat
        row,col=0,0
        ans=[[0 for i in range(c)] for i in range(r)]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                ans[row][col]=mat[i][j]
                col+=1
                if col==c:
                    row+=1
                    col=0
        return ans
                