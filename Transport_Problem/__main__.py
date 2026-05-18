"""
The Main method where I input the problem and test the methods:

1. Create and balance the problem.

2. Generate initial solutions (Northwest Corner, Minimum Cost, Vogel's Approximation Method).
3. Optimize with Stepping Stone.
4. Display results and graphs.
"""

import numpy as np
from data.transport_problem import TransportProblem
from methods.northwest_corner import NorthWestCorner
from methods.minimum_cost import MinimumCostMethod
from methods.vogel import VogelApproximation
from optimization.stepping_stone import SteppingStone
from visualization.visualizer import TransportVisualizer

def main():

    # Problem data
    costs = np.array([
        [5, 2, 7, 3],
        [3, 6, 6, 1],
        [6, 1, 2, 4],
        [4, 3, 6, 6]
    ], dtype=float)

    supply = np.array([80, 30, 60, 45], dtype=float)
    demand = np.array([70, 40, 70, 35], dtype=float)

    # Create problem and balance it
    problem = TransportProblem(costs, supply, demand)
    problem.balance_problem()

    # Northwest Corner Method
    nw_method = NorthWestCorner()
    nw_solution = nw_method.solve(problem)

    # Minimum Cost Method
    mc_method = MinimumCostMethod()
    mc_solution = mc_method.solve(problem)

    # Vogel method
    vg_method = VogelApproximation()
    vg_solution = vg_method.solve(problem)

    # Optimization with Stepping stone
    # For the Northwest Corner
    optimizer = SteppingStone()
    optimal_solution_NW, history = optimizer.optimize(nw_solution, problem)

    # For Minimum Cost
    optimizer = SteppingStone()
    optimal_solution_MC, history = optimizer.optimize(mc_solution, problem)

    # For Vogel
    optimizer = SteppingStone()
    optimal_solution_VG, history = optimizer.optimize(vg_solution, problem)

    # Visualization of results
    visualizer = TransportVisualizer()
    visualizer.show_assignment(nw_solution, problem, "Assignment — Northwest Corner")
    visualizer.show_assignment(mc_solution, problem, "Assignment — Minimum Cost")
    visualizer.show_assignment(vg_solution, problem, "Assignment — Vogel")
    visualizer.show_assignment(optimal_solution_NW, problem, "Assignment Optimal for Northwest Corner - Stepping Stone")
    visualizer.show_assignment(optimal_solution_MC, problem, "Optimal Assignment for Minimum Cost - Stepping Stone")
    visualizer.show_assignment(optimal_solution_VG, problem, "Optimal Assignment for Vogel-Stepping Stone")


if __name__ == "__main__":
    main()