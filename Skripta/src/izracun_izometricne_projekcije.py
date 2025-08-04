#! /bin/python3
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# --- 1. Definicija kotov ---
alpha_deg = 45
beta_deg = -35.264  # približno arccos(sqrt(2/3))

# - rotacija za dimetrično projekcijo
# alpha_deg = -20.74
# beta_deg = -19.47  # približno arccos(sqrt(2/3))

alpha = np.radians(alpha_deg)
beta = np.radians(beta_deg)

# --- 2. Rotacijski matriki ---
Rz = np.array([
    [np.cos(alpha), -np.sin(alpha), 0],
    [np.sin(alpha),  np.cos(alpha), 0],
    [0,              0,             1]
])

Rx = np.array([
    [1, 0, 0],
    [0, np.cos(beta), -np.sin(beta)],
    [0, np.sin(beta),  np.cos(beta)]
])

# --- 3. Projekcijska matrika (XZ projekcija) ---
P_XZ = np.array([
    [1, 0, 0],
    [0, 0, 0],
    [0, 0, 1]
])

# --- 4. Skupna transformacija ---
T = P_XZ @ Rx @ Rz

# --- 5. Osnovni vektorji ---
i = np.array([1, 0, 0])
j = np.array([0, 1, 0])
k = np.array([0, 0, 1])

# --- 6. Rotirani vektorji ---
i_rot = Rx @ Rz @ i
j_rot = Rx @ Rz @ j
k_rot = Rx @ Rz @ k

# --- 7. Projekcije rotiranih vektorjev ---
i_proj = T @ i
j_proj = T @ j
k_proj = T @ k

# --- 8. Prikaz ---
fig = plt.figure(figsize=(12,6))

# Levi graf: 3D pogled pred in po rotaciji
ax3d = fig.add_subplot(1, 2, 1, projection='3d')
ax3d.set_title("Vektorji pred in po rotaciji v 3D prostoru")

# Črtkani – osnovni
ax3d.quiver(0, 0, 0, *i, color='r', linestyle='dashed', label='i (osnovni)', arrow_length_ratio=0.1)
ax3d.quiver(0, 0, 0, *j, color='g', linestyle='dashed', label='j (osnovni)', arrow_length_ratio=0.1)
ax3d.quiver(0, 0, 0, *k, color='b', linestyle='dashed', label='k (osnovni)', arrow_length_ratio=0.1)

# Polne – rotirani
ax3d.quiver(0, 0, 0, *i_rot, color='r', label='i (rotiran)', arrow_length_ratio=0.1)
ax3d.quiver(0, 0, 0, *j_rot, color='g', label='j (rotiran)', arrow_length_ratio=0.1)
ax3d.quiver(0, 0, 0, *k_rot, color='b', label='k (rotiran)', arrow_length_ratio=0.1)

ax3d.scatter(0, 0, 0, color='black', s=30)
ax3d.set_xlim([-1, 1])
ax3d.set_ylim([-1, 1])
ax3d.set_zlim([-1, 1])
ax3d.set_xlabel('X')
ax3d.set_ylabel('Y')
ax3d.set_zlabel('Z')
ax3d.view_init(elev=25, azim=45)
ax3d.legend()

# Desni graf: projekcija v XZ ravnino
ax2d = fig.add_subplot(1, 2, 2)
ax2d.set_title("Projekcija vektorjev v ravnino XZ")

# Projekcije
ax2d.quiver(0, 0, i_proj[0], i_proj[2], angles='xy', scale_units='xy', scale=1, color='r', label='i projiciran')
ax2d.quiver(0, 0, j_proj[0], j_proj[2], angles='xy', scale_units='xy', scale=1, color='g', label='j projiciran')
ax2d.quiver(0, 0, k_proj[0], k_proj[2], angles='xy', scale_units='xy', scale=1, color='b', label='k projiciran')

# Osi in mreža
ax2d.axhline(0, color='gray', lw=0.5)
ax2d.axvline(0, color='gray', lw=0.5)
ax2d.scatter(0, 0, color='black', s=30)
ax2d.set_xlabel('X')
ax2d.set_ylabel('Z')
ax2d.axis('equal')
ax2d.grid(True)
ax2d.set_xlim(-1, 1.5)
ax2d.invert_xaxis() #obrnimo smer x osi, da sovpada s 3D prostorom
ax2d.set_ylim(-0.5, 1.5)
ax2d.legend()

plt.tight_layout()
plt.show()

