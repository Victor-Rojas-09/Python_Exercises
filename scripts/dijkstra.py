import heapq


def dijkstra(n, graph, start):
    """
    Dijkstra's Shortest Path Algorithm
    """

    # Initialize distances
    dist = [float("inf")] * n

    # Distance to source is zero
    dist[start] = 0

    # Create priority queue
    pq = [(0, start)]

    # Process nodes
    while pq:

        current_dist, node = heapq.heappop(pq)

        # Ignore outdated values
        if current_dist > dist[node]:
            continue

        # Explore neighbors
        for neighbor, weight in graph[node]:

            new_dist = current_dist + weight

            # Found shorter path
            if new_dist < dist[neighbor]:

                dist[neighbor] = new_dist

                heapq.heappush(
                    pq,
                    (new_dist, neighbor)
                )

    return dist


# ---------------------------------------------------
# Example usage
# ---------------------------------------------------

graph = {
    0: [(1, 4), (2, 1)],
    1: [(3, 1)],
    2: [(1, 2), (3, 5)],
    3: []
}

distances = dijkstra(
    n=4,
    graph=graph,
    start=0
)

print(distances)