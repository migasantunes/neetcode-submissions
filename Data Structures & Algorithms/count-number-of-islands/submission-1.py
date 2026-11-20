class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        count = 0

        def island(r, c):
            grid[r][c] = '0'
            if c + 1 < COLS and grid[r][c + 1] == '1':
                island(r, c + 1)
            if c - 1 >= 0 and grid[r][c - 1] == '1':
                island(r, c - 1)
            if r + 1 < ROWS and grid[r + 1][c] == '1':
                island(r + 1, c)
            if r - 1 >= 0 and grid[r - 1][c] == '1':
                island(r - 1, c)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1':
                    island(r, c)
                    count += 1

        return count