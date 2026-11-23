class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        ROWS, COLS = len(grid), len(grid[0])
    
        fresh = set()
        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh.add((r, c))
        
        mnts = 0
        while q and fresh:
            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    
                    if (nr < 0 or nc < 0 or 
                        nr >= ROWS or nc >= COLS or 
                        (nr, nc) not in fresh):
                        continue
                    
                    grid[nr][nc] = 2
                    fresh.remove((nr, nc))
                    q.append((nr, nc))

            mnts += 1

        return -1 if fresh else mnts