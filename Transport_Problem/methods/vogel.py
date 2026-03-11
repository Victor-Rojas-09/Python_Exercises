"""
Método de Aproximación de Vogel
"""

import numpy as np
from Transport_Problem.data.transport_problem import TransportProblem

class VogelApproximation:
    """
    Método de aproximación de Vogel para generar una solución inicial.
    """

    def solve(self, problem: TransportProblem) -> np.ndarray:
        """
        Parameters
        ----------
        problem : TransportProblem
            Instancia del problema de transporte.

        Returns
        -------
        np.ndarray
            Matriz de asignación inicial.
        """
        rows, cols = problem.costs.shape
        allocation = np.zeros((rows, cols))
        supply = problem.supply.copy()
        demand = problem.demand.copy()
        costs = problem.costs.copy()

        active_rows = [True] * rows
        active_cols = [True] * cols

        # Funciones para calcular penalización de fila y columna
        def row_penalty(row):
            vals = sorted(costs[row, c] for c in range(cols) if active_cols[c])
            return (vals[1] - vals[0]) if len(vals) >= 2 else 0

        def col_penalty(col):
            vals = sorted(costs[r, col] for r in range(rows) if active_rows[r])
            return (vals[1] - vals[0]) if len(vals) >= 2 else 0

        # Iteramos hasta agotar oferta y demanda
        for _ in range(rows + cols - 1):
            if supply.sum() < 1e-9 or demand.sum() < 1e-9:
                break

            penalties = (
                [(row_penalty(r), r, 'row') for r in range(rows) if active_rows[r]] +
                [(col_penalty(c), c, 'col') for c in range(cols) if active_cols[c]]
            )
            if not penalties:
                break

            # Seleccionamos la mayor penalización
            _, selected, kind = max(penalties, key=lambda x: x[0])

            if kind == 'row':
                row = selected
                column = min((c for c in range(cols) if active_cols[c]), key=lambda c: costs[row, c])
            else:
                column = selected
                row = min((r for r in range(rows) if active_rows[r]), key=lambda r: costs[r, column])

            assigned = min(supply[row], demand[column])
            allocation[row, column] = assigned

            # Reducimos oferta y demanda
            supply[row] -= assigned
            demand[column] -= assigned

            # Desactivamos fila o columna agotada
            if np.isclose(supply[row], 0):
                active_rows[row] = False
                costs[row, :] = np.inf
            if np.isclose(demand[column], 0):
                active_cols[column] = False
                costs[:, column] = np.inf

        return allocation
