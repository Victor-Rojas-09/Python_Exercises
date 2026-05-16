import pandas as pd
import numpy as np
from Transport_Problem.data.transport_problem import TransportProblem


class TransportVisualizer:
    """
    Class used to display transportation problem results.
    """

    def show_assignment(self, allocation: np.ndarray, problem: TransportProblem, title: str = "Assignment") -> None:
        """
        Display the allocation matrix as a formatted table.
        """

        if allocation.shape != problem.costs.shape:
            raise ValueError("Allocation matrix dimensions must match the cost matrix dimensions.")

        rows, cols = allocation.shape

        df = pd.DataFrame(
            allocation.astype(int),
            index=[f"Origin {r + 1}" for r in range(rows)],
            columns=[f"Destination {c + 1}" for c in range(cols)]
        )

        print(f"\n{title}")
        print(df.to_string())
        print(f"\nTotal Cost = {problem.total_cost(allocation):.2f}")

    def compare_solutions(self, initial: np.ndarray, optimal: np.ndarray, problem: TransportProblem) -> None:
        """
        Compare the initial and optimal solutions in tabular format.
        """
        if (
            initial.shape != problem.costs.shape or
            optimal.shape != problem.costs.shape
        ):
            raise ValueError(
                "Solution matrices must match the cost matrix dimensions."
            )

        print("\nINITIAL SOLUTION")
        self.show_assignment(
            allocation=initial,
            problem=problem,
            title="Initial Solution (Northwest Corner)"
        )

        print("\nOPTIMAL SOLUTION")
        self.show_assignment(
            allocation=optimal,
            problem=problem,
            title="Optimal Solution (Stepping Stone)"
        )