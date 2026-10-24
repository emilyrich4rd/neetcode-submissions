class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        maxX = len(board[0])
        maxY = len(board)
        minX = 0
        minY = 0
        visited = {}

        def search(i, x, y):
            if x >= maxX or y >= maxY or x < minX or y < minY:
                return False
            if visited.get((x,y)) == True:
                return False 
            if board[y][x] != word[i]:
                return False
            if i == len(word) - 1:
                return True

            visited[(x,y)] = True  

            positions = [(x+1, y), (x-1, y), (x,y+1), (x,y-1)]
            res = []
            for xPos, yPos in positions:
                res.append(search(i+1, xPos, yPos))
            visited[(x,y)] = False
            return any(res)
        
        for y in range(maxY):
            for x in range(maxX):
                if search(0, x, y):
                    return True
        return False