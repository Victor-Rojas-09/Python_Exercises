# Funcion promedio

def promedio_lista(numeros):
    if len(numeros) == 0:
        return 0  # Evito division por cero
    return sum(numeros) / len(numeros)

lista = [5, 8, 10, 3, 7]
promedio = promedio_lista(lista)
print(f"La lista es: {lista}")
print(f"El promedio es: {promedio}")