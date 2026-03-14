"""
Algoritmo Stepping Stone
"""

import numpy as np
from itertools import product
from Transport_Problem.data.transport_problem import TransportProblem

class SteppingStone:
    """
    The algorithm iteratively evaluates non-basic cells of a transportation
    solution and constructs improvement cycles. If a cycle yields a negative
    reduced cost, the allocation is adjusted to reduce total transportation
    cost.
    """

    def optimize(self, initial_solution: np.ndarray, problem: TransportProblem):
        """
        Optimize a feasible transportation solution using Stepping Stone.
        """

        rows, cols = problem.costs.shape
        allocation = initial_solution.copy().astype(float)

        history = []

        for iteration in range(1, 100):

            # Current transportation cost
            current_cost = problem.total_cost(allocation)

            # Compute reduced costs for non-basic cells
            reduced_costs = self.compute_reduced_costs(allocation, problem.costs)

            history.append({
                "iteration": iteration,
                "cost": current_cost,
                "allocation": allocation.copy()
            })

            # Check optimality condition
            negatives = {k: v for k, v in reduced_costs.items() if v < -1e-9}

            if not negatives:
                break

            # Select entering variable (most negative reduced cost)
            entering_cell = min(negatives, key=negatives.get)

            cycle = self.find_cycle(allocation, entering_cell, rows, cols)

            if cycle is None:
                break

            # Determine the minimum allocation on subtracting positions
            subtract_positions = [cycle[k] for k in range(1, len(cycle), 2)]

            theta = min(allocation[r, c] for r, c in subtract_positions)

            # Update allocations along the cycle
            for k, (r, c) in enumerate(cycle):

                if k % 2 == 0:
                    allocation[r, c] += theta
                else:
                    allocation[r, c] -= theta

                    if allocation[r, c] < 1e-9:
                        allocation[r, c] = 0.0

        return allocation, history

    def compute_reduced_costs(self, allocation: np.ndarray, costs: np.ndarray):
        """
        Compute reduced costs for all non-basic cells.
        A reduced cost represents the change in total cost if a unit
        is shipped through a currently unused route.
        """

        rows, cols = costs.shape

        basic_set = set(zip(*np.where(allocation > 0)))

        reduced_costs = {}

        for r, c in product(range(rows), range(cols)):

            if (r, c) in basic_set:
                continue

            cycle = self.find_cycle(allocation, (r, c), rows, cols)

            if cycle is None:
                continue

            delta = 0

            for k, (i, j) in enumerate(cycle):

                if k % 2 == 0:
                    delta += costs[i, j]
                else:
                    delta -= costs[i, j]

            reduced_costs[(r, c)] = round(delta, 8)

        return reduced_costs

    def find_cycle(self, allocation: np.ndarray, start, rows: int, cols: int):
        """
        Find a closed improvement cycle starting from a non-basic cell.
        The cycle alternates between horizontal and vertical moves
        through basic cells and must return to the starting position.
        """

        basic_set = set(zip(*np.where(allocation > 0)))

        # IMPORTANT: add entering cell temporarily
        basic_set.add(start)

        def dfs(path, search_row):

            r, c = path[-1]

            if search_row:

                for column in range(cols):

                    if column == c:
                        continue

                    candidate = (r, column)

                    if len(path) >= 4 and candidate == start:
                        return path

                    if candidate in basic_set and candidate not in path:
                        result = dfs(path + [candidate], False)

                        if result:
                            return result

            else:

                for row in range(rows):

                    if row == r:
                        continue

                    candidate = (row, c)

                    if len(path) >= 4 and candidate == start:
                        return path

                    if candidate in basic_set and candidate not in path:
                        result = dfs(path + [candidate], True)

                        if result:
                            return result

            return None

        return dfs([start], True)