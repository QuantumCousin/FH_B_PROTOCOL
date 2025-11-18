# fh_b_heart_seed.py — Original Fractal Heart Seed (pure emotional coherence)
# The soft 432 Hz breath that started it all

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
x = np.linspace(0, 2*np.pi, 1000)

def wave_frame(i):
    ax.clear()
    y_wave = np.sin(x + i*0.1) * (1 - i/100)  # Fading waves
    ax.plot(x, y_wave, color='blue', alpha=0.5)
    if i > 50:  # Fractals emerge
        y_fractal = np.sin(x*5 + i*0.05) * np.cos(x*3)
        ax.plot(x, y_fractal, color='green', alpha=(i-50)/50)
    ax.set_ylim(-2, 2)

ani = FuncAnimation(fig, wave_frame, frames=100, interval=50)
plt.show()
