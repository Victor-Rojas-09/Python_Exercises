"""
El Main donde ingreso el problema y pruebo los metodos: 
1. Crear el problema y balancearlo.
2. Generar soluciones iniciales (NW, Costo Mínimo, Vogel).
3. Optimizar con Stepping Stone.
4. Mostrar resultados y gráficos.
"""

import numpy as np
from data.transport_problem import TransportProblem
from methods.northwest_corner import NorthWestCorner
from methods.minimum_cost import MinimumCostMethod
from methods.vogel import VogelApproximation
from optimization.stepping_stone import SteppingStone
from visualization.visualizer import TransportVisualizer
from utils.cost_functions import total_cost

def main():
    # Datos del problema (ejemplo)
    costs = np.array([
        [5, 2, 7, 3],
        [3, 6, 6, 1],
        [6, 1, 2, 4],
        [4, 3, 6, 6]
    ], dtype=float)

    supply = np.array([80, 30, 60, 45], dtype=float)
    demand = np.array([70, 40, 70, 35], dtype=float)

    # Crear problema y balancearlo
    problem = TransportProblem(costs, supply, demand)
    problem.balance_problem()

    # Método 1: Esquina Noroeste
    nw_method = NorthWestCorner()
    nw_solution = nw_method.solve(problem)

    # Método 2: Costo Mínimo
    mc_method = MinimumCostMethod()
    mc_solution = mc_method.solve(problem)

    # Método 3: Vogel
    vg_method = VogelApproximation()
    vg_solution = vg_method.solve(problem)

    # Optimización con Stepping Stone (desde NW)
    optimizer = SteppingStone()
    optimal_solution, history = optimizer.optimize(nw_solution, problem)

    # Visualización de resultados
    visualizer = TransportVisualizer()
    visualizer.show_assignment(nw_solution, problem.costs, "Asignación — Esquina Noroeste")
    visualizer.show_assignment(mc_solution, problem.costs, "Asignación — Costo Mínimo")
    visualizer.show_assignment(vg_solution, problem.costs, "Asignación — Vogel")
    visualizer.show_assignment(optimal_solution, problem.costs, "Asignación Óptima Final")

    # Gráficos
    visualizer.plot_convergence(history)
    visualizer.compare_solutions(nw_solution, optimal_solution, problem.costs)

if __name__ == "__main__":
    main()
