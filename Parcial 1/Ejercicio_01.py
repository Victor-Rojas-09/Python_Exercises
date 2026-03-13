import numpy as np
import matplotlib.pyplot as plt

color_map = {
    "blanco": (255, 255, 255),
    "negro": (0, 0, 0),
    "rojo": (207, 52, 50),
    "amarillo": (254, 235, 53),
    "azul": (36, 168, 243),
    "verde": (80, 174, 77),
    "morado": (154, 42, 178),
    "naranja": (246, 169, 37),
    "beige": (254, 224, 188)
}

img = np.ones((17, 17, 3), dtype=np.uint8) * 255

def pintar(f, c_ini, c_fin, color):
    img[f, c_ini : c_fin + 1] = color_map[color]

pintar(1, 5, 7, "rojo")

pintar(2, 4, 5, "rojo")
pintar(2, 6, 7, "beige")
img[2,8] = color_map["rojo"]

pintar(3, 4, 5, "naranja")
img[3,6] = color_map["negro"]
img[3,7] = color_map["beige"]
img[3,8] = color_map["rojo"]

pintar(4, 4, 5, "naranja")
pintar(4, 6, 7, "beige")
img[4,8] = color_map["rojo"]

img[5,4] = color_map["naranja"]
img[5,5] = color_map["negro"]
img[5,6] = color_map["beige"]
pintar(5, 7, 9, "rojo")

img[6,5] = color_map["beige"]
pintar(6, 6, 9, "rojo")

pintar(7, 5, 7, "rojo")
pintar(7, 7, 8, "amarillo")
pintar(7, 4, 5, "rojo")




plt.imshow(img)

# Rejilla caiga entre pixeles
plt.xticks(np.arange(-0.5, 16, 1), [])
plt.yticks(np.arange(-0.5, 16, 1), [])

plt.grid(color='black', linestyle='-', linewidth=1) # Activa cuadricula
plt.tick_params(axis='both', which='both', length=0) # Quitar bordes
plt.show()