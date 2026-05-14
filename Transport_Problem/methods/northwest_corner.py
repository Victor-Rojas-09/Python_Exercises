import numpy as np
from Transport_Problem.data.transport_problem import TransportProblem

class NorthWestCorner:
    """
    Northwest corner method used to generate an initial feasible solution.
    """

    def solve(self, problem: TransportProblem) -> np.ndarray:
        """
        Solve the transportation problem using the northwest corner method..
        """

        rows, cols = problem.costs.shape

        allocation = np.zeros((rows, cols))
        supply = problem.supply.copy()
        demand = problem.demand.copy()

        row, column = 0, 0

        # Traverse the matrix starting from the upper-left corner
        while row < rows and column < cols:

            assigned = min(supply[row], demand[column])
            allocation[row, column] = assigned

            # Reduce supply and demand
            supply[row] -= assigned
            demand[column] -= assigned

            # Move according to which value is exhausted
            if np.isclose(supply[row], 0) and np.isclose(demand[column], 0):

                if row + 1 < rows:
                    row += 1

                else:
                    column += 1

            elif np.isclose(supply[row], 0):
                row += 1

            else:
                column += 1

        return allocation