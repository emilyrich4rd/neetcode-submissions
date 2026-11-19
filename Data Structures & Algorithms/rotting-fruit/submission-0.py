import copy
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        def inbounds(x, y):
            return x > -1 and x < len(grid[0]) and y > -1 and y < len(grid)

        rotted = set()
        n_fresh = 0
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == 2:
                    rotted.add((y,x))
                if grid[y][x] == 1:
                    n_fresh += 1
        mins = 0 
        if n_fresh == 0:
            return 0
        while True:
            mins += 1
            new_grid = copy.deepcopy(grid)
            new_positions = set()
            for (y,x) in rotted:
                if inbounds(x+1,y) and grid[y][x+1] == 1:
                    new_grid[y][x+1] = 2 
                    new_positions.add((y,x+1))
                    
                if inbounds(x-1,y) and grid[y][x-1] == 1:
                    new_grid[y][x-1] = 2
                    new_positions.add((y,x-1))

                if inbounds(x,y+1) and grid[y+1][x] == 1:
                    new_grid[y+1][x] = 2
                    new_positions.add((y+1,x))

                if inbounds(x,y-1) and grid[y-1][x] == 1:
                    new_grid[y-1][x] = 2
                    new_positions.add((y-1,x))
            n_fresh -= len(new_positions)

            rotted.update(new_positions)
            if n_fresh <= 0: # all rotten
                return mins 
            elif grid == new_grid: # not all rotten but nothing else can be done
                return -1
            grid = new_grid 