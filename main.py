import numpy as np
import pygame
import sys

from board import Board
from render import WINDOW_WIDTH, WINDOW_HEIGHT, BLACK, drawGrid, gridCellFromMousePos

def main():
    rows = 20
    columns = 20
    random_board = np.random.randint(0, 2, size=(rows, columns))
    global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(BLACK)
    board = Board(random_board)

    progress = False

    while True:
        drawGrid(board.board, SCREEN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    board.update_board()
                elif event.key == pygame.K_TAB:
                    progress = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_TAB:
                    progress = False
            
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                grid_pos = gridCellFromMousePos(pos, rows, columns)
                board.override_cell(grid_pos[0], grid_pos[1])

        if progress:
            board.update_board()
        pygame.display.update()
        CLOCK.tick(60)
    

if __name__ == "__main__":
    main()