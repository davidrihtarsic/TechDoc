#! /bin/python3

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 1. Osnovni vektorji
i = np.array([1, 0, 0])
j = np.array([0, 1, 0])
k = np.array([0, 0, 1])

# 2. Normalni vektor dimetrične projekcijske ravnine
n = np.array([1/3, np.sqrt(7)/3, 1/3])
n = n / np.linalg.norm(n)  # normaliziramo

# 3. Funkcija za ortogonalno projekcijo vektorja na ravnino
def project_onto_plane(v, n):
    return v - np.dot(v, n) * n

# 4. Projekcije osnovnih vektorjev
i_proj = project_onto_plane(i, n)
j_proj = project_onto_plane(j, n)
k_proj = project_onto_plane(k, n)

# 5. Priprava 3D grafa
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.set_title("Ortogonalna projekcija osnovnih vektorjev na dimetrično ravnino")

# 6. Osnovni vektorji
ax.quiver(0, 0, 0, *i, color='r', label='i', linewidth=1.5)
ax.quiver(0, 0, 0, *j, color='g', label='j', linewidth=1.5)
ax.quiver(0, 0, 0, *k, color='b', label='k', linewidth=1.5)

# 7. Projekcije osnovnih vektorjev
ax.quiver(0, 0, 0, *i_proj, color='r', linestyle='dashed', label="i'", arrow_length_ratio=0.05)
ax.quiver(0, 0, 0, *j_proj, color='g', linestyle='dashed', label="j'", arrow_length_ratio=0.05)
ax.quiver(0, 0, 0, *k_proj, color='b', linestyle='dashed', label="k'", arrow_length_ratio=0.05)

# 8. Normalni vektor
ax.quiver(0, 0, 0, *n, color='k', label='normalni vektor n', linewidth=2)

# 9. Ravnina: zračunamo y iz enačbe ravnine: n · r = 0
xx, zz = np.meshgrid(np.linspace(-1, 1, 10), np.linspace(-1, 1, 10))
yy = (-n[0]*xx - n[2]*zz) / n[1]
ax.plot_surface(xx, yy, zz, alpha=0.3, color='gray')

# 10. Osi in pogled
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_xlim([-1, 1])
ax.set_ylim([-1, 1])
ax.set_zlim([-1, 1])
ax.view_init(elev=25, azim=45)
ax.legend()
plt.tight_layout()
plt.show()

