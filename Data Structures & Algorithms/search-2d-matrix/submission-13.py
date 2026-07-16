class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0 
        h = len(matrix) - 1
        row = -1 
        if len(matrix) != 1:
            while l < h:
                mid_l = (l + h) // 2
                mid_h = mid_l + 1
                if mid_h >= len(matrix):
                    return False
                if target >= matrix[mid_l][0] and target < matrix[mid_h][0]:
                    row = mid_l 
                    break 
                if target == matrix[mid_h][0]:
                    row = mid_h
                    break 
                elif target > matrix[mid_h][0]:
                    l = mid_h 
                else:
                    h = mid_l 
        else:
            row = 0 

        if l == h:
            row = l 

        if row == -1:
            return False
        
        lst = matrix[row]
        l = 0 
        h = len(lst) - 1
        while l <= h:
            mid = (l + h) // 2
            if target == lst[mid]:
                return True 
            elif target < lst[mid]:
                h = mid - 1
            else:
                l = mid + 1
        return False
        