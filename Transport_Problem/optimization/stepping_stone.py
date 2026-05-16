import numpy as np
from itertools import product
from Transport_Problem.data.transport_problem import TransportProblem


class SteppingStone:
    """
    Stepping Stone optimization method for transportation problems.

    Features:
    - Correct cycle handling.
    - Proper reduced cost computation.
    - Correct theta updates.
    - Supports degeneracy through explicit basic variables.
    - Searches cycles in both directions.
    """

    def optimize(
        self,
        init_allocation: np.ndarray,
        problem: TransportProblem,
        basic_cells: set = None
    ):
        """
        Optimize a feasible transportation solution using
        the Stepping Stone method.
        """

        total_rows, total_columns = problem.costs.shape

        optimized_allocation = (
            init_allocation.copy().astype(float)
        )

        # If no explicit basis is provided,
        # use positive allocations as basics
        if basic_cells is None:

            basic_cells = set(
                zip(*np.where(optimized_allocation > 0))
            )

        history = []

        for iteration_number in range(1, 100):

            current_total_cost = problem.total_cost(
                optimized_allocation
            )

            history.append({
                "iteration": iteration_number,
                "cost": current_total_cost,
                "allocation": optimized_allocation.copy()
            })

            # Compute reduced costs
            reduced_costs = self.compute_reduced_costs(
                optimized_allocation,
                problem.costs,
                basic_cells
            )

            # Select improving moves
            improving_moves = {
                cell: value
                for cell, value in reduced_costs.items()
                if value < -1e-9
            }

            # Optimal solution reached
            if not improving_moves:
                break

            # Entering variable
            entering_cell = min(
                improving_moves,
                key=improving_moves.get
            )

            # Build cycle
            cycle = self.find_cycle(
                basic_cells,
                entering_cell,
                total_rows,
                total_columns
            )

            if cycle is None:
                break

            # remove repeated final node
            cycle_nodes = cycle[:-1]

            # Odd positions are subtracting cells
            subtracting_cells = [
                cycle_nodes[index]
                for index in range(1, len(cycle_nodes), 2)
            ]

            theta = min(
                optimized_allocation[row, col]
                for row, col in subtracting_cells
            )

            # Apply alternating updates
            for cycle_index, (row, col) in enumerate(cycle_nodes):

                if cycle_index % 2 == 0:

                    optimized_allocation[row, col] += theta

                else:

                    optimized_allocation[row, col] -= theta

                    # Numerical cleanup
                    if optimized_allocation[row, col] < 1e-9:
                        optimized_allocation[row, col] = 0.0

            # Update basis

            # Entering variable becomes basic
            basic_cells.add(entering_cell)

            # Remove ONE leaving variable
            for row, col in subtracting_cells:

                if abs(optimized_allocation[row, col]) < 1e-9:

                    if (row, col) != entering_cell:

                        basic_cells.remove((row, col))
                        break

        return optimized_allocation, history

    def compute_reduced_costs(self, allocation_matrix: np.ndarray, transportation_costs: np.ndarray, basic_cells: set):
        """
        Compute reduced costs for all non-basic cells.
        """

        total_rows, total_columns = transportation_costs.shape

        reduced_costs = {}

        for row_index, column_index in product(
            range(total_rows),
            range(total_columns)
        ):

            current_cell = (
                row_index,
                column_index
            )

            # Skip basic variables
            if current_cell in basic_cells:
                continue

            cycle = self.find_cycle(
                basic_cells,
                current_cell,
                total_rows,
                total_columns
            )

            if cycle is None:
                continue

            # IMPORTANT:
            # ignore repeated final node
            cycle_nodes = cycle[:-1]

            reduced_cost = 0.0

            for cycle_index, (
                cycle_row,
                cycle_column
            ) in enumerate(cycle_nodes):

                if cycle_index % 2 == 0:

                    reduced_cost += transportation_costs[
                        cycle_row,
                        cycle_column
                    ]

                else:

                    reduced_cost -= transportation_costs[
                        cycle_row,
                        cycle_column
                    ]

            reduced_costs[current_cell] = round(
                reduced_cost,
                8
            )

        return reduced_costs

    def find_cycle(self, basic_cells: set, start_cell, total_rows: int, total_columns: int):
        """
        Find a valid Stepping Stone cycle.
        """

        # Temporary graph including entering variable
        working_basic_cells = basic_cells.copy()
        working_basic_cells.add(start_cell)

        def dfs(current_path, search_horizontally):

            current_row, current_column = current_path[-1]

            # Horizontal moves
            if search_horizontally:

                for next_column in range(total_columns):

                    if next_column == current_column:
                        continue

                    candidate_cell = (
                        current_row,
                        next_column
                    )

                    # Close cycle
                    if (
                        candidate_cell == start_cell
                        and len(current_path) >= 4
                    ):
                        return current_path + [start_cell]

                    # Continue search
                    if (
                        candidate_cell in working_basic_cells
                        and candidate_cell not in current_path
                    ):

                        result = dfs(
                            current_path + [candidate_cell],
                            False
                        )

                        if result is not None:
                            return result

            # Vertical moves
            else:

                for next_row in range(total_rows):

                    if next_row == current_row:
                        continue

                    candidate_cell = (
                        next_row,
                        current_column
                    )

                    # Close cycle
                    if (
                        candidate_cell == start_cell
                        and len(current_path) >= 4
                    ):
                        return current_path + [start_cell]

                    # Continue search
                    if (
                        candidate_cell in working_basic_cells
                        and candidate_cell not in current_path
                    ):

                        result = dfs(
                            current_path + [candidate_cell],
                            True
                        )

                        if result is not None:
                            return result

            return None

        # try both initial directions
        return (
            dfs([start_cell], True)
            or
            dfs([start_cell], False)
        )