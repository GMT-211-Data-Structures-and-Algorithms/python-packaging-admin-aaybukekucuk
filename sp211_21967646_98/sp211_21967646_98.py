import heapq
import logging

# Logger ayarları
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

def set_log_level(level_name):
    level = getattr(logging, level_name.upper(), None)
    if not isinstance(level, int):
        raise ValueError(f'Invalid log level: {level_name}')
    logging.getLogger().setLevel(level)
    logger.info(f"Logging level set to {level_name}")
    logger.debug("Logging level set to DEBUG")

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
