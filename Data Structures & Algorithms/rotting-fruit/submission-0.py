class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # BFS obviously
        # go through the whole grid
        # only when we find a rotten banana we start the BFS
        # change rotten to 0
        # keep a seen bananas set
        # switch bananas to wrotten on every BFS pass
        # keep a iteration counter 
        # if at the end there are still bananas in the set return -1

        ROWS, COLS = len(grid), len(grid[0])
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        fresh = 0
        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append([r,c])

        minutes = 0
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append([nr,nc])
            minutes += 1
        return minutes if fresh == 0 else -1



        """
        def bfs(r, c):
            count = 0
            q = deque()
            q.append([r, c])
            
            while q:
                leng = len(q)
                hasPassed = False
                for i in range(leng):
                    r, c = q.popleft()
                    if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == 0:
                        continue
                    for dr, dc in directions:
                        q.append([r + dr, c + dc])

                    if (r,c) in seen: seen.remove((r,c))
                    grid[r][c] = 0
                    hasPassed = True

                if hasPassed: count += 1

            return count

        minM = 101
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    seen.add((r,c))
                elif grid[r][c] == 2:
                    minM = min(minM, bfs(r, c))
        
        return minM if not seen else -1
        """