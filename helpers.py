TRAVERSAL_DELAY = 20

def get_neighbors(cell, grid):
    neighbors = []
    rows, cols = len(grid), len(grid[0])

    if cell.row > 0:
        neighbors.append(grid[cell.row-1][cell.col])
    if cell.row < rows-1:
        neighbors.append(grid[cell.row + 1][cell.col])
    if cell.col > 0:
        neighbors.append(grid[cell.row][cell.col -1])
    if cell.col < cols-1:
        neighbors.append(grid[cell.row][cell.col +1])

    return neighbors

def trace_path(end, draw_func):
    current = end
    while current.previous:
        current = current.previous
        current.color = (255, 255, 0)
        draw_func()

