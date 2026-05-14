class DisjointSet:
    """
    This structure keeps track of connected components
    and efficiently detects cycles in a graph.
    """

    def __init__(self, number_of_nodes):
        # Initially, each node is its own parent
        self.parent = list(range(number_of_nodes))

        # Rank helps keep the tree shallow
        self.rank = [0] * number_of_nodes

    def find_root(self, node):
        """
        Find the representative (root) of a set.
        """

        if self.parent[node] != node:
            self.parent[node] = self.find_root(self.parent[node])

        return self.parent[node]

    def connect_sets(self, node_a, node_b):
        """
        Merge two sets if they are different.
        """

        root_a = self.find_root(node_a)
        root_b = self.find_root(node_b)

        # Same root means same connected component
        if root_a == root_b:
            return False

        # Union by rank optimization
        if self.rank[root_a] < self.rank[root_b]:
            self.parent[root_a] = root_b

        elif self.rank[root_a] > self.rank[root_b]:
            self.parent[root_b] = root_a

        else:
            self.parent[root_b] = root_a
            self.rank[root_a] += 1

        return True


def kruskal_minimum_spanning_tree(total_nodes, weighted_edges):
    """
    Kruskal's Minimum Spanning Tree Algorithm
    """

    # STEP 1: Sort edges
    weighted_edges.sort()

    # STEP 2: Create the Union-Find structure
    disjoint_set = DisjointSet(total_nodes)

    mst_edges = []
    total_weight = 0

    # STEP 3: Process edges in ascending weight order
    for edge_weight, source, destination in weighted_edges:

        # Try to connect both nodes
        if disjoint_set.connect_sets(source, destination):

            # Add edge to the MST
            mst_edges.append(
                (source, destination, edge_weight)
            )

            # Update total cost
            total_weight += edge_weight

    # Return final MST and total cost
    return mst_edges, total_weight


# ---------------------------------------------------
# Example usage
# ---------------------------------------------------

graph_edges = [
    (1, 0, 1),
    (4, 0, 2),
    (2, 1, 2),
    (5, 1, 3),
    (3, 2, 3)
]

mst, cost = kruskal_minimum_spanning_tree(
    total_nodes=4,
    weighted_edges=graph_edges
)

print("Minimum Spanning Tree:")
for edge in mst:
    print(edge)

print("Total Cost:", cost)