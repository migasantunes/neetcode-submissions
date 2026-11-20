class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        maxL = 0

        def island(r, c):
            if c < 0 or r < 0 or c >= COLS or r >= ROWS or grid[r][c] == 0:
                return 0

            res = 1
            grid[r][c] = 0
            for dr, dc in directions:
                res += island(r + dr,c + dc)
            return res
            
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    maxL = max(maxL, island(r, c))
        return maxL