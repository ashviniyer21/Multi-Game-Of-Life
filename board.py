class Board:
    
    def __init__(self, starting_board):
        self.board = starting_board

    def override_cell(self, r, c):
        if self.board[r, c] == 1:
            self.board[r, c] = 0
        else:
            self.board[r, c] = 1
    def _update_cell(self, r, c, temp_board):
        neighbor_count = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0 or r + i < 0 or c + j < 0 or r + i >= len(temp_board) or c + j >= len(temp_board[0]):
                    continue
                neighbor_count += temp_board[r + i, c + j] 

        if temp_board[r, c] == 0:
            if neighbor_count == 3:
                self.board[r, c] = 1
        else:
            if neighbor_count < 2 or neighbor_count > 3:
                self.board[r, c] = 0
    
    def update_board(self):
        temp_board = self.board.copy()
        for i in range(len(temp_board)):
            for j in range(len(temp_board[i])):
                self._update_cell(i, j ,temp_board)