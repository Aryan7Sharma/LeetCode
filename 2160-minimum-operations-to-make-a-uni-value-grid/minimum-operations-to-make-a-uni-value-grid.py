import statistics
class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        m = len(grid)
        n = len(grid[0])
        flattened_sorted = [num for row in grid for num in row]
        rows = len(grid)
        cols = len(grid[0])
        midValue = self.custom_median(flattened_sorted)
        modulo = midValue%x
        operation = 0
        for r in range(m):
            for c in range(n):
                currvalue = grid[r][c]
                if (currvalue%x)!=modulo:return -1
                operation+=abs(currvalue-midValue)/x
        return int(operation)
    def custom_median(self, arr):
        arr_sorted = sorted(arr)
        n = len(arr_sorted)
        mid_index = n // 2
        return arr_sorted[mid_index]

 