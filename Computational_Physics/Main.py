from exercises.free_fall import FreeFall
from exercises.unit_conversion import UnitConversion
from exercises.displacement import Displacement
from exercises.vectors import Vectors
from exercises.projectile import Projectile

def menu():
    print("\n--- MENU DE EJERCICIOS ---")
    print("1. Calculo de caida libre")
    print("2. Conversion de unidades de velocidad")
    print("3. Calculo del desplazamiento")
    print("4. Suma de vectores")
    print("5. Producto escalar y ángulo entre vectores")
    print("6. Lanzamiento de proyectil")
    print("7. Salir")

def main():
    while True:
        menu()
        option = input("Seleccione una opcion: ")

        try:
            if option == "1":
                h = float(input("Altura (m): "))
                print("Tiempo de caida:",
                      f"{FreeFall.calculate_time(h):.2f} s")

            elif option == "2":
                v = float(input("Velocidad: "))
                c = input("Tipo (km/h o m/s): ")

                if c == "km/h":
                    print(UnitConversion.kmh_to_ms(v), "m/s")
                elif c == "m/s":
                    print(UnitConversion.ms_to_kmh(v), "km/h")
                else:
                    print("Tipo invalido.")

            elif option == "3":
                u = float(input("Velocidad inicial (m/s): "))
                a = float(input("Aceleracion (m/s²): "))
                t = float(input("Tiempo (s): "))
                print("Desplazamiento:",
                      Displacement.calculate(u, a, t), "m")

            elif option == "4":
                v1 = list(map(float, input("Vector 1 (x y): ").split()))
                v2 = list(map(float, input("Vector 2 (x y): ").split()))
                print("Suma:", Vectors.add(v1, v2))

            elif option == "5":
                v1 = list(map(float, input("Vector 1 (x y): ").split()))
                v2 = list(map(float, input("Vector 2 (x y): ").split()))
                print("Producto escalar:", Vectors.dot_product(v1, v2))
                print("Angulo:", f"{Vectors.angle(v1, v2):.2f} °")

            elif option == "6":
                v0 = float(input("Velocidad inicial (m/s): "))
                angle = float(input("Angulo (grados): "))
                print("Alcance maximo:",
                      Projectile.max_range(v0, angle), "m")
                print("Altura maxima:",
                      Projectile.max_height(v0, angle), "m")

            elif option == "7":
                print("Programa finalizado.")
                break

            else:
                print("Opción invalida.")

        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    main()
