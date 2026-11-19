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
            new_positions = set()
            for (y,x) in rotted:
                for (x_, y_) in [(1,0), (-1,0), (0,1), (0,-1)]:
                    nx, ny = x_ + x, y_ + y
                    if inbounds(nx,ny) and grid[ny][nx] == 1:
                        grid[ny][nx] = 2
                        new_positions.add((ny,nx))
            n_fresh -= len(new_positions)

            rotted = new_positions
            if n_fresh == 0: # all rotten
                return mins 
            elif len(new_positions) == 0: # not all rotten but nothing else can be done
                return -1