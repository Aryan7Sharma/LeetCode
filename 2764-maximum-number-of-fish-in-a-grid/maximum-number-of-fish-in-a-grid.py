class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        rlen,clen = len(grid), len(grid[0])
        maxFish = 0
        def dfs(r, c, temp):
            if r<0 or r>=rlen or c<0 or c>=clen or grid[r][c] in [0,-1]:return 0
            fish = grid[r][c]
            grid[r][c] = -1
            temp+=(fish + dfs(r, c+1, temp) + dfs(r, c-1, temp) + dfs(r+1, c, temp) + dfs(r-1, c, temp))
            return temp
        
        for r in range(rlen):
            for c in range(clen):
                if grid[r][c]>0:maxFish = max(maxFish, dfs(r,c,0))
        return maxFish   
