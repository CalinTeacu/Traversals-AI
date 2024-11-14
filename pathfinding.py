import pygame
import random
from bfs import bfs
from dfs import dfs
from dijkstra import dijkstra
from astar import astar
from helpers import get_neighbors, trace_path



WIDTH, HEIGHT = 600, 600  
ROWS, COLS = 20, 20


WHITE, BLACK, GREEN, RED = (255, 255, 255), (0, 0, 0), (0, 255, 0), (255, 0, 0)


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pathfinding Visualizer")

class Cell:
    def __init__(self, row, col, size):
        self.row, self.col = row, col
        self.size = size
        self.x = col * size
        self.y = row * size
        self.color = WHITE
        self.is_start = False
        self.is_end = False
        self.is_obstacle = False
        self.previous = None

    def draw(self):
        if self.is_start:
            self.color = GREEN
        elif self.is_end:
            self.color = RED
        elif self.is_obstacle:
            self.color = BLACK
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))

def make_grid(rows, cols):
    grid = [[Cell(i, j, WIDTH // COLS) for j in range(cols)] for i in range(rows)]
    for row in grid:
        for cell in row:
            if random.random() < 0.2:  # 20% chance to be an obstacle
                cell.is_obstacle = True
    return grid

def draw_grid(grid):
    screen.fill(WHITE)
    for row in grid:
        for cell in row:
            cell.draw()

    cell_size = WIDTH // COLS
    for x in range(0, WIDTH, cell_size):
        pygame.draw.line(screen, BLACK, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, cell_size):
        pygame.draw.line(screen, BLACK, (0, y), (WIDTH, y))

    pygame.display.flip()

def main():
    grid = make_grid(ROWS, COLS)
    start, end = None, None
    running = True
    while running:
        draw_grid(grid)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                
                if pos[1] < HEIGHT:
                    row, col = pos[1] // (HEIGHT // ROWS), pos[0] // (WIDTH // COLS)
                    cell = grid[row][col]

                    if not start and not cell.is_obstacle:
                        start = cell
                        start.is_start = True
                    elif not end and cell != start and not cell.is_obstacle:
                        end = cell
                        end.is_end = True

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:  # Reset
                    start, end = None, None
                    grid = make_grid(ROWS, COLS)
                elif event.key == pygame.K_b and start and end:  # BFS
                    bfs(start, end, grid, lambda: draw_grid(grid))
                elif event.key == pygame.K_d and start and end:  # DFS
                    dfs(start, end, grid, lambda: draw_grid(grid))
                elif event.key == pygame.K_j and start and end:  # Dijkstra
                    dijkstra(start, end, grid, lambda: draw_grid(grid))
                elif event.key == pygame.K_a and start and end:  # A-star
                    astar(start, end, grid, lambda: draw_grid(grid))

    pygame.quit()

main()
