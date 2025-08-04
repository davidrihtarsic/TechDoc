import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Koti v stopinjah
alpha_deg = 60
beta_deg = -90

# Pretvori v radiane
alpha = np.radians(alpha_deg)
beta = np.radians(beta_deg)

# Izvorni vektor
e = np.array([8, 0, 0])

# Rotacijska matrika okoli osi Z
Rz = np.array([
    [np.cos(alpha), -np.sin(alpha), 0],
    [np.sin(alpha),  np.cos(alpha), 0],
    [0,              0,             1]
])

# Rotacijska matrika okoli osi Y
Ry = np.array([
    [np.cos(beta), 0, np.sin(beta)],
    [0,            1, 0],
    [-np.sin(beta),0, np.cos(beta)]
])

# Vmesni rezultat: rotacija okoli Z
e_rot_Z = Rz @ e

# Končni rezultat: še rotacija okoli Y
e_rot_YZ = Ry @ e_rot_Z

# --- GRAF ---
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_title('Rotacija vektorja v 3D prostoru')

# Izhodišče kot točka (črna pika)
ax.scatter(0, 0, 0, color='black', s=50, label='Izhodišče (0, 0, 0)')

# Izris vektorjev iz točke (0,0,0)
ax.quiver(0, 0, 0, *e, color='red', label='Originalni vektor')
ax.quiver(0, 0, 0, *e_rot_Z, color='blue', label='Po rotaciji okoli Z (α)')
ax.quiver(0, 0, 0, *e_rot_YZ, color='green', label='Po rotaciji Z → Y (α, β)')

# Nastavitve osi – da je izhodišče v spodnjem kotu
ax.set_xlim([0, 10])
ax.set_ylim([0, 10])
ax.set_zlim([0, 10])

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Postavitev pogleda
ax.view_init(elev=25, azim=45)
ax.legend()
plt.tight_layout()
plt.show()
