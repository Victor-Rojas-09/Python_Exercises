import numpy as np
from itertools import product
from Transport_Problem.data.transport_problem import TransportProblem


class SteppingStone:
    """
    Stepping Stone optimization method for transportation problems.

    The algorithm improves an initial feasible transportation plan by:
    1. Evaluating unused routes.
    2. Building improvement cycles.
    3. Moving flow through cycles that reduce total cost.
    4. Repeating until no further improvement is possible.
    """

    def optimize(self, init_allocation: np.ndarray, problem: TransportProblem
    ):
        """
        Optimize a feasible transportation solution using
        the Stepping Stone method.
        """

        total_rows, total_columns = problem.costs.shape

        optimized_allocation = init_allocation.copy().astype(float)

        history = []

        # Main optimization loop
        for iteration_number in range(1, 100):

            # Compute the current transportation cost
            current_total_cost = problem.total_cost(
                optimized_allocation
            )

            # Compute reduced costs for every non-basic cell
            reduced_costs = self.compute_reduced_costs(
                optimized_allocation,
                problem.costs
            )

            # Store iteration data for analysis/debugging
            history.append({
                "iteration": iteration_number,
                "cost": current_total_cost,
                "allocation": optimized_allocation.copy()
            })

            # Select all improving moves
            improving_moves = {
                cell_position: reduced_cost
                for cell_position, reduced_cost
                in reduced_costs.items()
                if reduced_cost < -1e-9
            }

            # If no negative reduced costs exist, the solution is optimal
            if not improving_moves:
                break

            # Select the entering cell with the
            # most negative reduced cost
            entering_cell = min(
                improving_moves,
                key=improving_moves.get
            )

            # Build the improvement cycle
            improvement_cycle = self.find_cycle(
                optimized_allocation,
                entering_cell,
                total_rows,
                total_columns
            )

            # If no valid cycle is found,
            # stop the optimization
            if improvement_cycle is None:
                break

            # Cells in odd positions are subtraction nodes
            subtracting_cells = [
                improvement_cycle[index]
                for index in range(1, len(improvement_cycle), 2)
            ]

            # Determine the maximum transferable flow
            # without violating feasibility
            theta = min(
                optimized_allocation[row_index, column_index]
                for row_index, column_index in subtracting_cells
            )

            # Update the transportation plan
            # by alternating additions/subtractions
            for cycle_index, (
                row_index,
                column_index
            ) in enumerate(improvement_cycle):

                # Even positions receive flow
                if cycle_index % 2 == 0:

                    optimized_allocation[
                        row_index,
                        column_index
                    ] += theta

                # Odd positions lose flow
                else:

                    optimized_allocation[
                        row_index,
                        column_index
                    ] -= theta

                    # Remove floating-point residuals
                    if (
                        optimized_allocation[
                            row_index,
                            column_index
                        ] < 1e-9
                    ):
                        optimized_allocation[
                            row_index,
                            column_index
                        ] = 0.0

        return optimized_allocation, history

    def compute_reduced_costs(
        self,
        allocation_matrix: np.ndarray,
        transportation_costs: np.ndarray
    ):
        """
        Compute reduced costs for all unused routes.

        The reduced cost represents how the total transportation
        cost would change if one unit were assigned to a currently
        unused route.
        """

        total_rows, total_columns = transportation_costs.shape

        # Basic cells are currently allocated routes
        basic_cells = set(
            zip(*np.where(allocation_matrix > 0))
        )

        reduced_costs = {}

        # Evaluate every non-basic cell
        for row_index, column_index in product(
            range(total_rows),
            range(total_columns)
        ):

            current_cell = (row_index, column_index)

            # Skip already allocated cells
            if current_cell in basic_cells:
                continue

            # Build an improvement cycle
            cycle = self.find_cycle(
                allocation_matrix,
                current_cell,
                total_rows,
                total_columns
            )

            # If no valid cycle exists,
            # the reduced cost cannot be computed
            if cycle is None:
                continue

            reduced_cost = 0

            # Compute alternating cost sum
            for cycle_index, (
                cycle_row,
                cycle_column
            ) in enumerate(cycle):

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

    def find_cycle(self, allocation_matrix: np.ndarray, start_cell, total_rows: int, total_columns: int):
        """
        Find a closed improvement cycle.

        The cycle:
        - starts from a non-basic cell,
        - alternates between horizontal and vertical moves,
        - traverses only basic cells,
        - returns to the starting position.
        """

        # Extract all currently allocated cells
        basic_cells = set(
            zip(*np.where(allocation_matrix > 0))
        )

        # Temporarily add the entering cell
        # so the cycle can be constructed
        basic_cells.add(start_cell)

        def dfs(current_path,search_horizontally
        ):
            """
            Recursive DFS (Depth First Search) used to construct
            alternating transportation cycles.
            """

            current_row, current_column = current_path[-1]

            # Horizontal exploration
            if search_horizontally:

                for next_column in range(total_columns):

                    if next_column == current_column:
                        continue

                    candidate_cell = (
                        current_row,
                        next_column
                    )

                    # A valid cycle must contain
                    # at least 4 nodes
                    if (
                        len(current_path) >= 4
                        and candidate_cell == start_cell
                    ):
                        return current_path + [start_cell]

                    # Continue dfs through
                    # valid unvisited basic cells
                    if (
                        candidate_cell in basic_cells
                        and candidate_cell not in current_path
                    ):

                        result = dfs(
                            current_path + [candidate_cell],
                            False
                        )

                        if result:
                            return result

            # Vertical exploration
            else:

                for next_row in range(total_rows):

                    if next_row == current_row:
                        continue

                    candidate_cell = (
                        next_row,
                        current_column
                    )

                    if (
                        len(current_path) >= 4
                        and candidate_cell == start_cell
                    ):
                        return current_path + [start_cell]

                    if (
                        candidate_cell in basic_cells
                        and candidate_cell not in current_path
                    ):

                        result = dfs(
                            current_path + [candidate_cell],
                            True
                        )

                        if result:
                            return result

            # No valid continuation found
            return None

        return dfs([start_cell], True)