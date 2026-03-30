class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        DIR = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        self.total_peremiter = 0

        def dfsCallPeremiter(r, c):
            self.total_peremiter += getPeremiter(r, c)
            grid[r][c] = 2

            for dir_r, dir_c in DIR:
                target_r = r + dir_r
                target_c = c + dir_c

                if target_r < ROWS and target_c < COLS and target_r > -1 and target_c > -1 and grid[target_r][target_c] == 1:
                    dfsCallPeremiter(target_r, target_c)

        def getPeremiter(r, c):
            peremiter_count = 0

            for dir_r, dir_c in DIR:
                target_r = r + dir_r
                target_c = c + dir_c

                if target_r >= ROWS or target_c >= COLS or target_r < 0 or target_c < 0:
                    peremiter_count += 1
                elif grid[target_r][target_c] == 0:
                    peremiter_count += 1

            return peremiter_count
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    dfsCallPeremiter(r, c)
                    break
        
        return self.total_peremiter
        



                

        