"""
Clase TransportProblem y función total_cost
"""

import numpy as np

class TransportProblem:
    """
    Clase que modela un problema clásico de transporte.
    
    Parameters
    ----------
    costs : np.ndarray
        Matriz de costos de transporte.
    supply : np.ndarray
        Vector de oferta.
    demand : np.ndarray
        Vector de demanda.
    """

    def __init__(self, costs: np.ndarray, supply: np.ndarray, demand: np.ndarray):
        self.costs = costs.astype(float)
        self.supply = supply.astype(float)
        self.demand = demand.astype(float)

    def is_balanced(self) -> bool:
        """
        Verifica si el problema está balanceado.
        
        Returns
        -------
        bool
            True si oferta = demanda, False en caso contrario.
        """
        return np.isclose(self.supply.sum(), self.demand.sum())

    def balance_problem(self) -> None:
        """
        Balancea el problema agregando un origen o destino ficticio.
        """
        total_supply = self.supply.sum()
        total_demand = self.demand.sum()

        if np.isclose(total_supply, total_demand):
            return

        if total_supply > total_demand:
            diff = total_supply - total_demand
            self.demand = np.append(self.demand, diff)
            self.costs = np.hstack([self.costs, np.zeros((self.costs.shape[0], 1))])
        else:
            diff = total_demand - total_supply
            self.supply = np.append(self.supply, diff)
            self.costs = np.vstack([self.costs, np.zeros((1, self.costs.shape[1]))])


# ──────────────────────────────────────────────────────────
# Función auxiliar: costo total
# ──────────────────────────────────────────────────────────
def total_cost(allocation: np.ndarray, costs: np.ndarray) -> float:
    """
    Calcula el costo total de una asignación.

    Parameters
    ----------
    allocation : np.ndarray
        Matriz de asignación.
    costs : np.ndarray
        Matriz de costos.

    Returns
    -------
    float
        Costo total de la asignación.
    """
    return float((allocation * costs).sum())
