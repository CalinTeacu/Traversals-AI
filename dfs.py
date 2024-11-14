import pygame
from helpers import get_neighbors, trace_path, TRAVERSAL_DELAY

def dfs(start, end, grid, draw_func):
    stack = [start]
    visited = set()
    visited.add(start)

    while stack:
        current = stack.pop()

        if current == end:
            trace_path(end, draw_func)
            return

        for neighbor in get_neighbors(current, grid):
            if neighbor not in visited and not neighbor.is_obstacle:
                visited.add(neighbor)
                neighbor.previous = current  
                stack.append(neighbor)
                neighbor.color = (255, 182, 193)  

                pygame.time.delay(TRAVERSAL_DELAY)
                draw_func()

        if current != start:
            current.color = (200, 200, 200) 
