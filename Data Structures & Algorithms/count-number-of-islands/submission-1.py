class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        x_bound = len(grid[0])
        y_bound = len(grid)

        def dfs(x, y):
            if x < 0 or x >= x_bound or y < 0 or y >= y_bound:
                return False
            if grid[y][x] == "0":
                return False
            else:
                grid[y][x] = "0"
                dfs(x-1, y)
                dfs(x+1, y)
                dfs(x, y+1)
                dfs(x, y-1)
                return True
        
        count = 0
        for row in range(y_bound):
            for col in range(x_bound):
                island = dfs(col, row)
                if island == True:
                    count += 1
        return count