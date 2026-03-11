"""
Método de Costo Mínimo
"""

import numpy as np
from data.transport_problem import TransportProblem

class MinimumCostMethod:
    """
    Método de costo mínimo para generar una solución inicial.
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

        # Mientras haya oferta y demanda por asignar
        while supply.sum() > 1e-9 and demand.sum() > 1e-9:
            # Seleccionamos la celda con menor costo disponible
            mask = (costs < np.inf)
            if not mask.any():
                break

            row, column = np.unravel_index(np.where(mask, costs, np.inf).argmin(), costs.shape)
            assigned = min(supply[row], demand[column])
            allocation[row, column] = assigned

            # Reducimos oferta y demanda
            supply[row] -= assigned
            demand[column] -= assigned

            # Si se agotó la oferta de la fila, bloqueamos esa fila
            if np.isclose(supply[row], 0):
                costs[row, :] = np.inf
            # Si se agotó la demanda de la columna, bloqueamos esa columna
            if np.isclose(demand[column], 0):
                costs[:, column] = np.inf

        return allocation
