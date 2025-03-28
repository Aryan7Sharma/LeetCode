from typing import List
import heapq

class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        m, n = len(grid), len(grid[0])
        queries_with_index = sorted((q, i) for i, q in enumerate(queries))  # Sort queries to process in increasing order
        result = [0] * len(queries)
        visited = [[False] * n for _ in range(m)]
        min_heap = [(grid[0][0], 0, 0)]  # Min heap stores (cell value, row, col)
        visited[0][0] = True
        count = 0  # Keeps track of visited cells
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
        
        for q, idx in queries_with_index:
            while min_heap and min_heap[0][0] < q:  # Expand the reachable area
                value, r, c = heapq.heappop(min_heap)
                count += 1  # Increment count for this cell
                
                for dr, dc in directions:  # Explore 4 possible directions
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc]:
                        heapq.heappush(min_heap, (grid[nr][nc], nr, nc))
                        visited[nr][nc] = True
            
            result[idx] = count  # Store result in original query order
        
        return result
