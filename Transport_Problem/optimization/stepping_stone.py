"""
Algoritmo Stepping Stone
"""

import numpy as np
from itertools import product
from Transport_Problem.data.transport_problem import TransportProblem

class SteppingStone:
    """
    Algoritmo Stepping Stone para optimizar soluciones de transporte.
    """

    def optimize(self, initial_solution: np.ndarray, problem: TransportProblem):
        """
        Parameters
        ----------
        initial_solution : np.ndarray
            Solución inicial factible.
        problem : TransportProblem
            Instancia del problema de transporte.
        """
        rows, cols = problem.costs.shape
        allocation = initial_solution.copy().astype(float)
        history = []

        for iteration in range(1, 100):
            # Usamos el metodo de TransportProblem correctamente
            current_cost = problem.total_cost(allocation)
            reduced_costs = self.compute_reduced_costs(allocation, problem.costs)

            history.append({
                'iteration': iteration,
                'cost': current_cost,
                'allocation': allocation.copy()
            })

            # Si no hay costos reducidos negativos, alcanzamos la solución óptima
            negatives = {k: v for k, v in reduced_costs.items() if v < -1e-9}
            if not negatives:
                break

            # Seleccionamos la celda entrante con menor costo reducido
            entering = min(negatives, key=negatives.get)
            cycle = self.find_cycle(allocation, entering, rows, cols)

            if cycle is None:
                break

            # Calculamos theta (mínima cantidad que se puede ajustar en el ciclo)
            positions_to_reduce = [cycle[k] for k in range(1, len(cycle), 2)]
            theta = min(allocation[r, c] for r, c in positions_to_reduce)

            # Ajustamos asignaciones en el ciclo
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
        Calcula los costos reducidos para celdas no básicas.
        """
        rows, cols = costs.shape
        basic_set = set(zip(*np.where(allocation > 0)))
        reduced = {}

        for row, column in product(range(rows), range(cols)):
            if (row, column) in basic_set:
                continue
            cycle = self.find_cycle(allocation, (row, column), rows, cols)
            if cycle is None:
                continue
            delta = sum(costs[r, c] * (1 if k % 2 == 0 else -1)
                        for k, (r, c) in enumerate(cycle))
            reduced[(row, column)] = round(delta, 8)

        return reduced

    def find_cycle(self, allocation: np.ndarray, start, rows: int, cols: int):
        """
        Encuentra un ciclo cerrado que pasa por la celda entrante.
        """
        basic_set = set(zip(*np.where(allocation > 0)))

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
