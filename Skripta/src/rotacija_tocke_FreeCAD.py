import numpy as np
import Part
from FreeCAD import Vector

kot_deg = 45
kot_rad = np.radians(kot_deg)

Rz = np.array([
    [np.cos(kot_rad), -np.sin(kot_rad), 0],
    [np.sin(kot_rad),  np.cos(kot_rad), 0],
    [0,                0,               1]
])

print("Rotacijska matrika Rz:")
print(Rz)

v = Vector(10, 0, 0)
izvorna_tocka = Part.show(Part.Vertex(v))
izvorna_tocka.ViewObject.PointColor = (0.0, 0.0, 1.0)
izvorna_tocka.ViewObject.PointSize = 8
izvorna_tocka.Label = "IzvornaTočka"

# pretvorba v numpy objekt
p = np.array([v.x, v.y, v.z])
# ROTACIJA = množenje matrike in točke
p_rot = Rz @ p

v_rot = Vector(*p_rot)
rotirana_tocka = Part.show(Part.Vertex(v_rot))
rotirana_tocka.ViewObject.PointColor = (1.0, 0.0, 0.0)
rotirana_tocka.ViewObject.PointSize = 8
rotirana_tocka.Label = "RotiranaTočka"

# Črta med točkama – SIVA
crta = Part.makeLine(v, v_rot)
crta_obj = Part.show(crta)
crta_obj.ViewObject.LineColor = (0.5, 0.5, 0.5)
crta_obj.Label = "Povezava"
