"""
Clase para la Visualización de resultados
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from Transport_Problem.data.transport_problem import TransportProblem

class TransportVisualizer:
    """
    Clase para visualizar resultados del problema de transporte.
    """

    def show_assignment(self, allocation: np.ndarray, problem: TransportProblem, title: str = "Asignación") -> None:
        """
        Muestra la matriz de asignación como tabla.

        Parameters
        ----------
        allocation : np.ndarray
            Matriz de asignación.
        problem : TransportProblem
            Instancia del problema de transporte.
        title : str
            Título de la tabla.
        """
        rows, cols = allocation.shape
        df = pd.DataFrame(
            allocation.astype(int),
            index=[f"Origen {r+1}" for r in range(rows)],
            columns=[f"Destino {c+1}" for c in range(cols)]
        )

        print(f"\n{title}")
        print(df.to_string())
        print(f" Costo total = {problem.total_cost(allocation):.2f}")

    def plot_convergence(self, history: list[dict]) -> None:
        """
        Grafica la evolución del costo total en cada iteración.

        Parameters
        ----------
        history : list of dict
            Historial de iteraciones con costo y asignación.
        """
        iterations = [h['iteration'] for h in history]
        costs = [h['cost'] for h in history]

        plt.figure(figsize=(8, 4))
        plt.plot(iterations, costs, marker='o', color='steelblue', linewidth=2.5)
        for i, c in zip(iterations, costs):
            plt.annotate(f"{c:.0f}", (i, c), textcoords="offset points",
                         xytext=(0, 10), ha='center', fontsize=9, fontweight='bold')
        plt.xlabel("Iteración")
        plt.ylabel("Costo Total")
        plt.title("Convergencia del Algoritmo Stepping Stone", fontsize=12, fontweight='bold')
        plt.grid(alpha=0.35)
        plt.tight_layout()
        plt.show()

    def compare_solutions(self, initial: np.ndarray, optimal: np.ndarray, problem: TransportProblem) -> None:
        """
        Compara gráficamente la solución inicial y la óptima.

        Parameters
        ----------
        initial : np.ndarray
            Solución inicial.
        optimal : np.ndarray
            Solución óptima.
        problem : TransportProblem
            Instancia del problema de transporte.
        """
        rows, cols = problem.costs.shape
        fig, axes = plt.subplots(1, 2, figsize=(14, 5))

        for ax, allocation, title in zip(
            axes,
            [initial, optimal],
            [f"Inicial (NW)\nCosto = {problem.total_cost(initial):.0f}",
             f"Óptima (Stepping Stone)\nCosto = {problem.total_cost(optimal):.0f}"]
        ):
            ax.imshow(allocation, cmap='Blues', aspect='auto', vmin=0)
            ax.set_title(title, fontsize=11, fontweight='bold')
            ax.set_xticks(range(cols))
            ax.set_xticklabels([f"D{c+1}" for c in range(cols)], fontsize=10)
            ax.set_yticks(range(rows))
            ax.set_yticklabels([f"O{r+1}" for r in range(rows)], fontsize=10)

            # Mostramos valores y costos dentro de cada celda
            for row in range(rows):
                for column in range(cols):
                    val = int(allocation[row, column])
                    cost = int(problem.costs[row, column])
                    text = f"{val}\n(c={cost})"
                    color = 'white' if val > 60 else 'black'
                    weight = 'bold' if val > 0 else 'normal'
                    ax.text(column, row, text, ha='center', va='center',
                            fontsize=9, color=color, fontweight=weight)

        plt.tight_layout()
        plt.show()
