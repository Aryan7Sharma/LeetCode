class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        pInteg = set()
        nInteg = set()
        res = []
        board = [["."]*n for i in range(n)]
        def backtrack(r):
            if(n==r):
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            for c in range(n):
                if c in col or (r+c) in pInteg or (r-c) in nInteg:
                    continue
                col.add(c)
                pInteg.add(r+c)
                nInteg.add(r-c)
                board[r][c]="Q"
                backtrack(r+1)
                col.remove(c)
                pInteg.remove(r+c)
                nInteg.remove(r-c)
                board[r][c]="."
        backtrack(0)
        return res
        