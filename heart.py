import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

x_right = np.linspace(0.01, np.sqrt(3) - 0.01, 500)
x_left = -x_right[::-1]

x_full = np.concatenate((x_left, x_right))

fig, ax = plt.subplots(figsize=(6, 6))
line, = ax.plot([], [], color='crimson', linewidth=2)

ax.set_xlim(-2, 2)
ax.set_ylim(-1, 3)
ax.set_aspect('equal')
ax.grid(True)
ax.axhline(0, color='black', linewidth=0.5)
ax.axvline(0, color='black', linewidth=0.5)
ax.set_title('PulseGraph', fontsize=14)

def init():
    line.set_data([], [])
    return line,

def animate(k):
    y_right = (x_right ** (2/3)) + 0.9 * np.sin(k * x_right) * np.sqrt(3 - x_right**2)
    y_left = (np.abs(x_left) ** (2/3)) + 0.9 * np.sin(k * x_left) * np.sqrt(3 - x_left**2)
    y_full = np.concatenate((y_left, y_right))
    line.set_data(x_full, y_full)
    return line,

ani = FuncAnimation(
    fig, animate,
    frames=np.linspace(0, 100, 200),
    init_func=init,
    blit=True,
    interval=50
)


plt.show()
