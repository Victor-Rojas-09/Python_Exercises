import numpy as np
from Transport_Problem.data.transport_problem import TransportProblem

class MinimumCostMethod:
    """
    Minimum cost method used to generate an initial feasible solution.
    """

    def solve(self, problem: TransportProblem) -> np.ndarray:
        """
        Solve the transportation problem using the minimum cost method.
        """

        rows, cols = problem.costs.shape

        allocation = np.zeros((rows, cols))
        supply = problem.supply.copy()
        demand = problem.demand.copy()
        costs = problem.costs.copy()

        # Continue while there is remaining supply and demand
        while supply.sum() > 1e-9 and demand.sum() > 1e-9:

            # Select the available cell with the minimum cost
            mask = (costs < np.inf)

            if not mask.any():
                break

            row, column = np.unravel_index(np.where(mask, costs, np.inf).argmin(), costs.shape)
            assigned = min(supply[row], demand[column])
            allocation[row, column] = assigned

            # Reduce supply and demand
            supply[row] -= assigned
            demand[column] -= assigned

            # Block row if supply is exhausted
            if np.isclose(supply[row], 0):
                costs[row, :] = np.inf

            # Block column if demand is exhausted
            if np.isclose(demand[column], 0):
                costs[:, column] = np.inf

        return allocation