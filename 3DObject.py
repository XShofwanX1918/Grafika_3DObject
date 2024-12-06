import plotly.graph_objects as go
import numpy as np

# Titik-titik dari limas segiempat
# Titik puncak
top = np.array([0, 0, 3])

# Titik-titik dasar segiempat
base = np.array([[-2, -2, 0],
                 [ 2, -2, 0],
                 [ 2,  2, 0],
                 [-2,  2, 0]])

# Membuat koordinat segiempat
x_base = base[:, 0]
y_base = base[:, 1]
z_base = base[:, 2]

# Koordinat titik-titik dari limas
x = np.append(x_base, top[0])
y = np.append(y_base, top[1])
z = np.append(z_base, top[2])

# Membuat segitiga untuk tiap sisi limas
i = [0, 1, 2, 3]
j = [1, 2, 3, 0]
k = [4, 4, 4, 4]

# Membuat plot 3D
fig = go.Figure(data=[go.Mesh3d(
    x=x, y=y, z=z,
    i=i, j=j, k=k,
    opacity=0.5,
    color='yellow'
)])

# Mengatur layout
fig.update_layout(
    scene=dict(
        xaxis_visible=False,
        yaxis_visible=False,
        zaxis_visible=False
    ),
    margin=dict(l=0, r=0, b=0, t=0),
    title="Limas Segiempat 3D"
)

# Animasi rotasi otomatis
fig.update_layout(updatemenus=[dict(
    type="buttons",
    showactive=False,
    buttons=[dict(label="Play",
                  method="animate",
                  args=[None, dict(frame=dict(duration=50, redraw=True), fromcurrent=True)])]
)])

# Menampilkan gambar
fig.show()
