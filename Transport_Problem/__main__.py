"""
El Main donde ingreso el problema y pruebo los metodos: 
1. Crear el problema y balancearlo.
2. Generar soluciones iniciales (NW, Costo Mínimo, Vogel).
3. Optimizar con Stepping Stone.
4. Mostrar respipultados y gráficos.
"""

import numpy as np
from data.transport_problem import TransportProblem
from methods.northwest_corner import NorthWestCorner
from methods.minimum_cost import MinimumCostMethod
from methods.vogel import VogelApproximation
from optimization.stepping_stone import SteppingStone
from visualization.visualizer import TransportVisualizer

def main():
    # Datos del problema
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

    # Metodo de la Esquina Noroeste
    nw_method = NorthWestCorner()
    nw_solution = nw_method.solve(problem)

    # Metodo del Costo Mínimo
    mc_method = MinimumCostMethod()
    mc_solution = mc_method.solve(problem)

    # Metodo de Vogel
    vg_method = VogelApproximation()
    vg_solution = vg_method.solve(problem)

    # Optimizacion con Stepping Stone
    # Para la Esquina Noroeste
    optimizer = SteppingStone()
    optimal_solution_NW, history = optimizer.optimize(nw_solution, problem)

    # Para Costo Minimo
    optimizer = SteppingStone()
    optimal_solution_MC, history = optimizer.optimize(mc_solution, problem)

    # Para Vogel
    optimizer = SteppingStone()
    optimal_solution_VG, history = optimizer.optimize(vg_solution, problem)

    # Visualizacion de resultados
    visualizer = TransportVisualizer()
    visualizer.show_assignment(nw_solution, problem, "Asignación — Esquina Noroeste")
    visualizer.show_assignment(mc_solution, problem, "Asignación — Costo Mínimo")
    visualizer.show_assignment(vg_solution, problem, "Asignación — Vogel")
    visualizer.show_assignment(optimal_solution_NW, problem, "Asignación Óptima para Esquina Noroeste - Stepping Stone")
    visualizer.show_assignment(optimal_solution_MC, problem, "Asignación Óptima para Costo Mínimo - Stepping Stone")
    visualizer.show_assignment(optimal_solution_VG, problem, "Asignación Óptima Para Vogel- Stepping Stone")

    # Graficos
    visualizer.plot_convergence(history)
    visualizer.compare_solutions(nw_solution, optimal_solution_VG, problem)

if __name__ == "__main__":
    main()
