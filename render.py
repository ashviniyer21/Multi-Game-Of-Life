import pygame

BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
GRAY = (100, 100, 100)
RED = (200, 0, 0)
COLORS = [WHITE, RED]
WINDOW_HEIGHT = 500
WINDOW_WIDTH = 500
BORDER = 20

def drawGrid(grid, screen):
    blockSize = min((WINDOW_HEIGHT - BORDER) / len(grid), (WINDOW_WIDTH - BORDER) / len(grid[0])) #Set the size of the grid block
    for r in range(0, len(grid)):
        for c in range(0, len(grid[r])):
            rect = pygame.Rect(c * blockSize + 1 + BORDER / 2, r * blockSize - 1 + BORDER / 2, blockSize - 2, blockSize - 2)
            color = COLORS[grid[r, c]]
            pygame.draw.rect(screen, color, rect)

def gridCellFromMousePos(pos, rows, cols):
    blockSize = min((WINDOW_HEIGHT - BORDER) / rows, (WINDOW_WIDTH - BORDER) / cols) #Set the size of the grid block
    return (int((pos[1] - BORDER / 2) // blockSize), int((pos[0] - BORDER / 2) // blockSize))