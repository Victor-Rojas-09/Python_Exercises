"""
Método Esquina Noroeste
"""

import numpy as np
from Transport_Problem.data.transport_problem import TransportProblem
class NorthWestCorner:
    """
    Método de la esquina noroeste para generar una solución inicial.
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

        row, column = 0, 0
        # Recorremos la matriz desde la esquina superior izquierda
        while row < rows and column < cols:
            assigned = min(supply[row], demand[column])
            allocation[row, column] = assigned

            # Reducimos oferta y demanda
            supply[row] -= assigned
            demand[column] -= assigned

            # Avanzamos según cuál se agotó
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
