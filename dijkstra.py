import heapq
from helpers import get_neighbors, trace_path, TRAVERSAL_DELAY
import pygame


def dijkstra(start, end, grid, draw_func):
    # Initialize distance for each cell to a large number
    for row in grid:
        for cell in row:
            cell.distance = float('inf')
    start.distance = 0

    # Priority queue for cells to explore, with distance as the priority
    priority_queue = [(0, id(start), start)]
    visited = set()

    while priority_queue:
        # Get the cell with the smallest distance
        current_distance, _, current = heapq.heappop(priority_queue)

        # If we've reached the end, trace back the path
        if current == end:
            trace_path(end, draw_func)
            return

        # Skip cells that are already visited
        if current in visited:
            continue

        # Mark the current cell as visited
        visited.add(current)

        # Explore neighbors
        for neighbor in get_neighbors(current, grid):
            if neighbor not in visited and not neighbor.is_obstacle:
                # Calculate the tentative distance to this neighbor
                tentative_distance = current_distance + 1

                # If this path to neighbor is shorter, update the distance
                if tentative_distance < neighbor.distance:
                    neighbor.distance = tentative_distance
                    neighbor.previous = current  # Track the path
                    heapq.heappush(priority_queue, (tentative_distance, id(neighbor), neighbor))
                    neighbor.color = (173, 216, 230)  # Light blue for explored cells

        # Visualize the process
        pygame.time.delay(TRAVERSAL_DELAY)
        draw_func()
