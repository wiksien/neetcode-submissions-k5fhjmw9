from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        DIRECTIONS = [[0, 1], [0, -1], [-1, 0], [1, 0]]

        def bfsCleanIsland(r, c):
            queue = deque([(r, c)])
            grid[r][c] = "0"
            while queue:
                cur_row, cur_col = queue.popleft()

                for direction in DIRECTIONS:
                    dr = cur_row + direction[0]
                    dc = cur_col + direction[1]

                    if dr < 0 or dr == ROWS or dc < 0 or dc == COLS:
                        continue
                
                    land_value = grid[dr][dc]

                    if land_value == "1":
                        grid[dr][dc] = "0"
                        queue.append([dr, dc])

        result = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    bfsCleanIsland(r, c)
                    result += 1
        

        return result
                


            
        