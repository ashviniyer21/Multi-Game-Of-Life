class Board:
    
    def __init__(self, starting_board, factions):
        self.board = starting_board
        self.factions = factions

    def override_cell(self, r, c):
        self.board[r, c] += 1
        if self.board[r, c] > self.factions:
            self.board[r, c] = 0
    def _update_cell(self, r, c, temp_board):
        neighbor_counts = [0] * (self.factions + 1)
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0 or r + i < 0 or c + j < 0 or r + i >= len(temp_board) or c + j >= len(temp_board[0]):
                    continue
                neighbor_counts[temp_board[r + i, c + j]] += 1

        if temp_board[r, c] == 0:
            multiple = False
            col = -1
            for i in range(1, len(neighbor_counts)):
                if neighbor_counts[i] == 3:
                    if col != -1:
                        multiple = True
                    col = i
            if multiple:
                self.board[r, c] = 0
            elif col != -1:
                self.board[r, c] = col
        else:
            curr_col = temp_board[r, c]
            for i in range(1, len(neighbor_counts)):
                if neighbor_counts[i] >= 4: # Dies if any faction surrounds it with 4+ (overpopulation or killing)
                    self.board[r, c] = 0
                    return

            if neighbor_counts[curr_col] >= 3: # Will maintain current faction
                return
            multiple = False
            new_col = -1
            for i in range(1, len(neighbor_counts)):
                if neighbor_counts[i] == 3: 
                    if new_col != -1:
                        multiple = True
                    new_col = i
            if multiple: # Cannot change color, collision
                self.board[r, c] = 0
                return
            elif new_col != -1: # Influenced to change color
                self.board[r, c] = new_col
                return
            
            if neighbor_counts[curr_col] >= 2: # Will maintain current faction
                return
            multiple = False
            new_col = -1
            for i in range(1, len(neighbor_counts)):
                if neighbor_counts[i] == 2: 
                    if new_col != -1:
                        multiple = True
                    new_col = i
            if multiple: # Cannot change color, collision
                self.board[r, c] = 0
                return
            elif new_col != -1: # Influenced to change color
                self.board[r, c] = new_col
                return
            
            self.board[r, c] = 0
        

    
    def update_board(self):
        temp_board = self.board.copy()
        for i in range(len(temp_board)):
            for j in range(len(temp_board[i])):
                self._update_cell(i, j ,temp_board)