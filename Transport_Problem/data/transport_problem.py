import numpy as np

class TransportProblem:
    """
    Clase que modela un problema clásico de transporte.
    """

    def __init__(self, costs: np.ndarray, supply: np.ndarray, demand: np.ndarray):
        self.costs = costs.astype(float)
        self.supply = supply.astype(float)
        self.demand = demand.astype(float)

    def is_balanced(self) -> bool:
        """
        Verifica si el problema está balanceado.
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

    def total_cost(self, allocation: np.ndarray) -> float:
        """
        Calcula el costo total de una asignación.
        """
        return float((allocation * self.costs).sum())
