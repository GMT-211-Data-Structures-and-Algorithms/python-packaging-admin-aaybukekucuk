import heapq
import logging

# Logging ayarları
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def dijkstra(graph, start):
    logger.info(f"Starting Dijkstra from node: {start}")
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]

    while pq:
        current_distance, current_node = heapq.heappop(pq)
        logger.debug(f"Visiting node: {current_node} with current distance: {current_distance}")

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                logger.info(f"Updating distance of node {neighbor} to {distance}")
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

def set_log_level(level_name):
    """Change the logging level dynamically."""
    level = getattr(logging, level_name.upper(), logging.INFO)
    logger.setLevel(level)
    logger.info(f"Logging level set to {level_name.upper()}")
