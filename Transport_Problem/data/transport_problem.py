import numpy as np

class TransportProblem:
    """
    Class that models a classical transportation problem.
    """

    def __init__(self, costs: np.ndarray, supply: np.ndarray, demand: np.ndarray):

        self.costs = costs.astype(float)
        self.supply = supply.astype(float)
        self.demand = demand.astype(float)

    def is_balanced(self) -> bool:
        """
        Check whether the transportation problem is balanced.
        """

        return np.isclose(self.supply.sum(), self.demand.sum())

    def balance_problem(self) -> None:
        """
        Balance by adding a dummy source or destination when necessary.
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
        Compute the total transportation cost for a given allocation.
        """

        return float((allocation * self.costs).sum())