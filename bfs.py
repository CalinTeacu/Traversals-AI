from collections import deque
from helpers import get_neighbors, trace_path, TRAVERSAL_DELAY

import pygame

def bfs(start, end, grid, draw_func):
    queue = deque([start])
    visited = set()
    visited.add(start)

    while queue:
        current = queue.popleft()

        if current == end:
            trace_path(end, draw_func)
            return
        
        for neighbor in get_neighbors(current, grid):
            if neighbor not in visited and not neighbor.is_obstacle:
                visited.add(neighbor)
                neighbor.previous = current
                queue.append(neighbor)
                neighbor.color = (173, 216, 230)

        pygame.time.delay(TRAVERSAL_DELAY)
        draw_func()