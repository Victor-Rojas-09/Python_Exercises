# Funcion paridad

def par_o_impar(numero):
    if numero % 2 == 0:
        return "Par"
    else:
        return "Impar"

n = int(input("Ingrese un número: "))
resultado = par_o_impar(n)
print(f"El número {n} es {resultado}.")
