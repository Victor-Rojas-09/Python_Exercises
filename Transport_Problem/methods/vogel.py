import numpy as np
from Transport_Problem.data.transport_problem import TransportProblem

class VogelApproximation:
    """
    Vogel approximation method used to generate an initial feasible solution.
    """

    def solve(self, problem: TransportProblem) -> np.ndarray:
        """
        Functions to compute row and column penalties
        """

        rows, cols = problem.costs.shape

        allocation = np.zeros((rows, cols))
        supply = problem.supply.copy()
        demand = problem.demand.copy()
        costs = problem.costs.copy()

        active_rows = [True] * rows
        active_cols = [True] * cols

        # Functions to compute row and column penalties
        def row_penalty(row):
            """
            Calculate row penalties.
            """

            vals = sorted(costs[row, c] for c in range(cols) if active_cols[c])

            return (vals[1] - vals[0]) if len(vals) >= 2 else 0

        def col_penalty(col):
            """
            Calculate column penalties.
            """

            vals = sorted(costs[r, col] for r in range(rows) if active_rows[r])

            return (vals[1] - vals[0]) if len(vals) >= 2 else 0

        # # Iterate until supply and demand are exhausted
        for _ in range(rows + cols - 1):
            if supply.sum() < 1e-9 or demand.sum() < 1e-9:
                break

            penalties = (
                [(row_penalty(r), r, 'row') for r in range(rows) if active_rows[r]] +
                [(col_penalty(c), c, 'col') for c in range(cols) if active_cols[c]]
            )
            if not penalties:
                break

            # Select the highest penalty
            _, selected, kind = max(penalties, key=lambda x: x[0])

            if kind == 'row':
                row = selected
                column = min((c for c in range(cols) if active_cols[c]), key=lambda c: costs[row, c])
            else:
                column = selected
                row = min((r for r in range(rows) if active_rows[r]), key=lambda r: costs[r, column])

            assigned = min(supply[row], demand[column])
            allocation[row, column] = assigned

            # Reduce supply and demand
            supply[row] -= assigned
            demand[column] -= assigned

            # Deactivate exhausted row or column
            if np.isclose(supply[row], 0):
                active_rows[row] = False
                costs[row, :] = np.inf

            if np.isclose(demand[column], 0):
                active_cols[column] = False
                costs[:, column] = np.inf

        return allocation