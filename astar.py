import heapq
from helpers import get_neighbors, trace_path, TRAVERSAL_DELAY
import pygame


def heuristic(cell, end):
    return abs(cell.row - end.row) + abs(cell.col - end.col)

def astar(start, end, grid, draw_func):
    for row in grid:
        for cell in row:
            cell.g_score = float('inf')
            cell.f_score = float('inf')
    start.g_score = 0
    start.f_score = heuristic(start, end)

    priority_queue = [(start.f_score, id(start), start)]
    visited = set()

    while priority_queue:

        current_f_score, _, current = heapq.heappop(priority_queue)

      
        if current == end:
            trace_path(end, draw_func)
            return
   
        if current in visited:
            continue

        visited.add(current)

        for neighbor in get_neighbors(current, grid):
            if neighbor not in visited and not neighbor.is_obstacle:
                tentative_g_score = current.g_score + 1

                if tentative_g_score < neighbor.g_score:
                    neighbor.g_score = tentative_g_score
                    neighbor.f_score = tentative_g_score + heuristic(neighbor, end)
                    neighbor.previous = current 

                    heapq.heappush(priority_queue, (neighbor.f_score, id(neighbor), neighbor))
                    neighbor.color = (144, 238, 144)  

        pygame.time.delay(TRAVERSAL_DELAY)
        draw_func()
