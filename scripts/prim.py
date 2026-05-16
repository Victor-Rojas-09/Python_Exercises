import heapq


def prim(n, graph, start=0):
    """
    Prim's Minimum Spanning Tree Algorithm
    """

    # STEP 1: Initialize structures
    visited = [False] * n

    mst = []

    total_cost = 0

    # STEP 2: Create priority queue
    pq = [(0, start, -1)]

    # STEP 3: Process edges
    while pq:

        weight, node, parent = (
            heapq.heappop(pq)
        )

        # Ignore visited nodes
        if visited[node]:
            continue

        visited[node] = True

        # Add edge to MST
        if parent != -1:

            mst.append(
                (parent, node, weight)
            )

            total_cost += weight

        # Explore neighbors
        for neighbor, edge_weight in graph[node]:

            if not visited[neighbor]:

                heapq.heappush(
                    pq,
                    (edge_weight, neighbor, node)
                )

    return mst, total_cost


# ---------------------------------------------------
# Example usage
# ---------------------------------------------------

graph = {
    0: [(1, 1), (2, 4)],
    1: [(0, 1), (2, 2), (3, 5)],
    2: [(0, 4), (1, 2), (3, 3)],
    3: [(1, 5), (2, 3)]
}

mst, cost = prim(
    n=4,
    graph=graph
)

print("Minimum Spanning Tree:")
for edge in mst:
    print(edge)

print("Total Cost:", cost)