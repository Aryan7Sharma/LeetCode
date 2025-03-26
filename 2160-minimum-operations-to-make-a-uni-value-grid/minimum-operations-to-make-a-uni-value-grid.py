class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        m = len(grid)
        n = len(grid[0])
        flattened_sorted = sorted([num for row in grid for num in row])
        rows = len(grid)
        cols = len(grid[0])
        sortedGrid = [flattened_sorted[i * cols:(i + 1) * cols] for i in range(rows)]
        midValue = sortedGrid[m//2][0] if m%2==0  else sortedGrid[m//2][n//2]
        modulo = midValue%x
        operation = 0
        for r in range(m):
            for c in range(n):
                currvalue = sortedGrid[r][c]
                if (currvalue%x)!=modulo:return -1
                operation+=abs(currvalue-midValue)/x
        return int(operation)

 