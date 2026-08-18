class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        my_dict = {}
        ROWS = len(board)
        COLS = len(board[0])
    
        length = len(board)
    
        current_row = 0
    
    
        while current_row < ROWS:
        
            for col in range(len(board[current_row])):
                value = board[current_row][col]
    
                if value.isdecimal():
                    if f"row{current_row}value{value}" in my_dict:
                        return False
                    else:
                        my_dict[f"row{current_row}value{value}"] = True
    
                    if f"column{col}value{value}" in my_dict:
                        return False
                    else:
                        my_dict[f"column{col}value{value}"] = True
    
                    if f"{grid_id_helper(current_row, col)}value{value}" in my_dict:
                          return False
                    else:
                        my_dict[f"{grid_id_helper(current_row, col)}value{value}"] = True
    
            current_row += 1
        return True

def grid_id_helper(row, col):

    #first row of 3 grids
    if row < 3:
        if col < 3:
            return "Grid1"
        if col > 5: 
            return "Grid3"
        else:
            return "Grid2"
        
    #second row of 3 grids
    if row >= 3 and row < 6:
        if col < 3:
            return "Grid4"
        if col > 5: 
            return "Grid6"
        else:
            return "Grid5"

    if row >= 6:
        if col < 3:
            return "Grid7"
        if col > 5: 
            return "Grid9"
        else:
            return "Grid8"
        